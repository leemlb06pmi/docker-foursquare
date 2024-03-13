import os

from flask import Flask, jsonify
from postgres import Postgres

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')

@app.route('/locations')
def locations():
    locations = [{
        'id': 1, 'name': 'los tacos numero uno dos tres'
    }]
    return jsonify({'locations': locations})
