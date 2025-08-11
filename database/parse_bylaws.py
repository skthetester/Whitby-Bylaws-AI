
import os
import json
import logging
from pathlib import Path
from PyPDF2 import PdfReader

RAW_DIR = Path(__file__).parent / "raw_bylaws"
OUT_DIR = Path(__file__).parent / "bylaws_json"
OUT_DIR.mkdir(exist_ok=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger("parse_bylaws")

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(str(pdf_path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return pages
    except Exception as e:
        logger.error(f"Failed to extract text from {pdf_path}: {e}")
        return []

def build_json(pdf_path, pages):
    # Simple schema for Hugging Face transformers (customize as needed)
    return {
        "file_name": pdf_path.name,
        "num_pages": len(pages),
        "pages": pages
    }

def parse_bylaws():
    pdf_files = list(RAW_DIR.glob("*.pdf"))
    logger.info(f"Found {len(pdf_files)} PDF files in {RAW_DIR}")
    for pdf_path in pdf_files:
        out_path = OUT_DIR / (pdf_path.stem + ".json")
        if out_path.exists():
            logger.info(f"Skipping {pdf_path.name}, JSON already exists.")
            continue
        logger.info(f"Processing {pdf_path.name}")
        pages = extract_text_from_pdf(pdf_path)
        if not pages:
            logger.warning(f"No text extracted from {pdf_path.name}")
            continue
        data = build_json(pdf_path, pages)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved {out_path.name}")

if __name__ == "__main__":
    parse_bylaws()
