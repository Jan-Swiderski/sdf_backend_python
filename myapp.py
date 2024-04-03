from flask import (Flask, jsonify)
import os
from dotenv import load_dotenv
from flask_cors import CORS
import queries

load_dotenv()
app = Flask(__name__)
CORS(app)
app.secret_key=os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return "Welcome to SDF!"

@app.route('/api_v1/serv-proj/all', methods=['GET'])
def get_all_serv_proj():
    data = queries.get_all_serv_proj()
    return jsonify(data)

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 8082,
        debug = True
    )
