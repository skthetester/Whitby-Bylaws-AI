from flask import Blueprint, request, jsonify
from sentence_transformers import SentenceTransformer
import chromadb
from transformers import pipeline
import os

routes = Blueprint("routes", __name__)
client = chromadb.PersistentClient(path="/app/database/chroma-data")
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
    bylaws = [r["metadatas"][0]["bylaw_number"] for r in results["metadatas"]]
    response = nlp(f"Explain bylaws {', '.join(bylaws)} in simple language: {query}", max_length=200)
    return jsonify({"laymans_answer": response[0]["generated_text"]})

@routes.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})