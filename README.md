# Whitby-Bylaws-AI

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
- `backend/`: Flask backend and static demo UI
- `database/`: Bylaws data and scripts

## Notes
- The `/api/ask` endpoint is a placeholder for AI integration.
- Add your bylaw data to `database/bylaws.json`.