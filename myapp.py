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

@app.route('/api_v1/serv-proj/<serv_proj_id>/poi/all', methods=['GET'])
def get_pois_by_serv_proj_id(serv_proj_id):
    serv_proj_id = serv_proj_id
    data = queries.get_pois_by_serv_proj_id(serv_proj_id)
    return jsonify(data)

@app.route('/api_v1/serv-proj/poi/<poi_id>/sub-poi/all', methods=['GET'])
def get_sub_pois_by_poi_id(poi_id):
    poi_id = poi_id
    data = queries.get_sub_pois_by_poi_id(poi_id)
    return jsonify(data)

@app.route('/api_v1/serv-proj/poi/sub-poi/<sub_poi_id>/events/all', methods=['GET'])
def get_sub_pois_events_by_sub_poi_id(sub_poi_id):
    sub_poi_id = sub_poi_id
    data = queries.get_sub_pois_events_by_sub_poi_id(sub_poi_id)
    return jsonify(data)

@app.route('/api_v1/serv-proj/poi/sub-poi/<sub_poi_id>/data/all', methods=['GET'])
def get_sub_pois_data_by_sub_poi_id(sub_poi_id):
    sub_poi_id = sub_poi_id
    data = queries.get_sub_pois_data_by_sub_poi_id(sub_poi_id)
    return jsonify(data)

@app.route('/api_v1/serv-proj/poi/sub-poi/events/<event_id>/images/all', methods=['GET'])
def get_images_by_sub_poi_event_id(event_id):
    event_id = event_id
    data = queries.get_images_by_sub_poi_event_id(event_id)
    return jsonify(data)

@app.route('/api_v1/serv-proj/poi/sub-poi/events/all/images/all', methods=['GET'])
def get_all_images():
    data = queries.get_all_images()
    return jsonify(data)

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 8082,
        debug = True
    )
