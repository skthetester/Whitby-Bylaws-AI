[![Netlify Status](https://api.netlify.com/api/v1/badges/f377409c-fd05-4799-a6fc-63d44144ed06/deploy-status)](https://app.netlify.com/projects/whitby-bylaws-ai/deploys)

A demo project for querying Whitby bylaws using an AI backend (Flask).

## Project Structure

```
Whitby-Bylaws-AI/
├── backend/
│   ├── app/
│   │   ├── static/
│   │   │   ├── public_demo.html
│   │   │   ├── public_demo.css
│   │   │   ├── public_demo.js
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
├── database/
│   ├── bylaws.json
│   ├── init_chroma.py
│   ├── parse_bylaws.py
├── .gitignore
├── README.md
├── build-backend.sh
├── docker-compose.yml
```

## Quick Start

1. **Build and run with Docker Compose:**
   ```sh
   ./build-backend.sh
   ```
   or (on Windows)
   ```sh
   docker-compose up --build
   ```

2. **Access the demo:**
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## Folders

## Notes
# Whitby-Bylaws-AI

A demo project for querying Whitby bylaws using an AI backend and vector search.

## Project Structure

- `backend/`: Flask backend and static demo UI
- `database/`: Bylaws data, scripts, and vector DB
- `database/raw_bylaws/`: Source PDF bylaws
- `database/bylaws_json/`: Extracted bylaw JSONs (for ML/embedding)
- `database/init_chroma.py`: Generate embeddings and store in ChromaDB
- `database/parse_bylaws.py`: Convert PDFs to JSON

## Quick Start

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Parse bylaws PDFs to JSON:**
   ```sh
   python database/parse_bylaws.py
   ```

3. **Generate embeddings and store in ChromaDB:**
   ```sh
   python database/init_chroma.py
   ```

4. **Run the backend (Flask):**
   ```sh
   cd backend
   python main.py
   ```

## Requirements
- Python 3.8+
- See `requirements.txt` for Python libraries

## Notes
- Embeddings use Hugging Face's `sentence-transformers/all-MiniLM-L6-v2` (free, lightweight)
- Vector DB is ChromaDB (local, persistent)
- JSONs in `bylaws_json/` are suitable for Hugging Face transformers and other ML workflows
- `.env` files and ChromaDB data are gitignored