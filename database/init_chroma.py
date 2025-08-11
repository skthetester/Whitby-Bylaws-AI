
from sentence_transformers import SentenceTransformer
import chromadb
import json
from pathlib import Path

def initialize_chroma():
    # Setup ChromaDB persistent client and collection
    client = chromadb.PersistentClient(path="database/chroma-data")
    collection = client.get_or_create_collection("bylaws")

    # Load the embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Directory containing per-bylaw JSONs
    BYLAW_JSON_DIR = Path(__file__).parent / "bylaws_json"
    bylaw_files = list(BYLAW_JSON_DIR.glob("*.json"))
    print(f"Found {len(bylaw_files)} bylaw JSON files.")

    for i, bylaw_path in enumerate(bylaw_files):
        with open(bylaw_path, encoding="utf-8") as f:
            bylaw = json.load(f)
        # Join all pages into a single string for embedding
        content = "\n".join(bylaw.get("pages", []))
        embedding = model.encode(content).tolist()
        # Use file name as bylaw_number, status is optional
        bylaw_number = bylaw.get("file_name", bylaw_path.stem)
        collection.add(
            documents=[content],
            metadatas=[{"bylaw_number": bylaw_number}],
            ids=[str(i)]
        )
        if (i+1) % 10 == 0:
            print(f"Processed {i+1} bylaws...")
    print("Done generating embeddings and storing in ChromaDB.")

if __name__ == "__main__":
    initialize_chroma()
