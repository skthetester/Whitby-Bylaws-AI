import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BYLAWS_URL = "https://www.whitby.ca/Modules/Bylaws/Bylaw"
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'database', 'raw_bylaws')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def sanitize_filename(name):
    return re.sub(r'[^\w\-\(\)\[\] ]+', '', name).strip().replace(' ', '_')

def download_pdfs():
    print(f"Fetching bylaws page: {BYLAWS_URL}")
    resp = requests.get(BYLAWS_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    bylaw_blocks = soup.find_all('a', href=True)
    count = 0
    for a in bylaw_blocks:
        href = a['href']
        if not href.startswith('/Modules/Bylaws/Bylaw/Download'):
            continue
        # Try to get bylaw number and name from the text before the download link
        parent = a.find_parent('li') or a.find_parent('div') or a.parent
        text = parent.get_text(separator=' ', strip=True) if parent else a.text
        # Try to extract bylaw number (e.g., By-law No. 8056-24)
        match = re.search(r'By-law No\.\s*([\w\-]+)', text)
        bylaw_number = match.group(1) if match else 'unknown'
        # Find the bylaw name from the Details link before the Download link
        bylaw_name = None
        prev = a.find_previous('a', href=True)
        while prev:
            if prev['href'].startswith('/Modules/Bylaws/Bylaw/Details'):
                bylaw_name = prev.text.strip()
                break
            prev = prev.find_previous('a', href=True)
        if not bylaw_name:
            # fallback to previous logic
            name_match = re.search(r'Download (.+?)(?: By-law)?$', a.text.strip())
            bylaw_name = name_match.group(1) if name_match else a.text.strip()
        # Build filename (no date)
        filename = f"{bylaw_number}_{sanitize_filename(bylaw_name)}.pdf"
        dest = os.path.join(DOWNLOAD_DIR, filename)
        if os.path.exists(dest):
            print(f"Already downloaded: {filename}")
            continue
        url = urljoin(BYLAWS_URL, href)
        print(f"Downloading {filename} ...")
        r = requests.get(url)
        if r.headers.get('content-type', '').lower() != 'application/pdf' and not filename.lower().endswith('.pdf'):
            print(f"Warning: {filename} does not appear to be a PDF.")
        with open(dest, 'wb') as f:
            f.write(r.content)
        count += 1
        # TEST CODE: Stop after downloading the first file
        if count == 1:
            print("Test mode: Stopping after first download.")
            break
    print(f"Download complete. {count} new files downloaded.")

if __name__ == "__main__":
    download_pdfs()
