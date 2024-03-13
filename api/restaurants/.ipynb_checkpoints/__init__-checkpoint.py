from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/locations')
def locations():
    locations = [{'country': 'France', 'city': 'Paris',
              'coordinates': '48.856614,2.352222'},
               {'country': 'Iceland', 'city': 'Reykjavík',
                'coordinates': '64.126521,-21.817439'}]
    return jsonify(locations)
