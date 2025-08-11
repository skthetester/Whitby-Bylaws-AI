from flask import Blueprint, request, jsonify

bp = Blueprint('api', __name__)

@bp.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query = data.get('query', '')
    # TODO: Integrate with AI/LLM backend
    answer = f"You asked: {query} (demo response)"
    return jsonify({'answer': answer})
