from flask import Blueprint, request, jsonify
from sentence_transformers import SentenceTransformer
import chromadb
from transformers import pipeline

routes = Blueprint("routes", __name__)
client = chromadb.PersistentClient(path="../database/chroma-data")
collection = client.get_collection("bylaws")
model = SentenceTransformer("all-MiniLM-L6-v2")
nlp = pipeline("text-generation", model="distilgpt2")

@routes.route("/api/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")
    status = data.get("bylaw_status", "active")
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=5, where={"status": status})
    bylaws = [r["bylaw_number"] for r in results["metadatas"][0]] if results["metadatas"] else []
    if bylaws:
        response = nlp(f"Explain bylaws {', '.join(bylaws)} in simple language: {query}", max_length=200)
        layman = response[0]["generated_text"]
    else:
        layman = "No relevant bylaws found."
    return jsonify({"laymans_answer": layman, "bylaws": bylaws})

@routes.route("/api/bylaw/<bylaw_number>", methods=["GET"])
def get_bylaw(bylaw_number):
    results = collection.query(query_texts=[bylaw_number], n_results=1)
    return jsonify(results["metadatas"][0][0] if results["metadatas"] else {"error": "Bylaw not found"})
