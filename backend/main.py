from flask import Flask
from flask_cors import CORS
from app.routes import routes

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://whitby-bylaws-ai.netlify.app"]}})
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)