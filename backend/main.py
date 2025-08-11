from flask import Flask, send_from_directory
from app.routes import bp
import os

app = Flask(__name__, static_folder='app/static', template_folder='app/templates')
app.register_blueprint(bp)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'public_demo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
