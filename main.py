from flask import Flask, current_app, request
from flask_cors import CORS, cross_origin

from analytics.artist_analytics import artists_json
from analytics.genre_analytics import genre_json
from analytics.tracks_analytics import tracks_json


# CORS init and Flask app setup
app = Flask(__name__)
cors = CORS(app, supports_credentials=True, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


# STATIC ROUTES
@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    return current_app.send_static_file('top_artists.html')


@app.route('/raw_track', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def items():
    return current_app.send_static_file('top_tracks.html')


# LIVE ROUTES

# GET ROUTES
@app.route('/genres', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def genres():
    return genre_json


@app.route('/artists', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def artists():
    return artists_json


@app.route('/tracks', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def tracks():
    return tracks_json


# POST ROUTES
@app.route('/json/user-token', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def user_token():
    data = request.json
    print(data)
    f = open('.cache', 'w')
    f.write(f"{data}")
    f.close()
    # f = open('.cache', 'r')
    # cache = f.read()
    # f.close()
    return data


# @app.route('/token/', methods=['GET'])
# @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
# def callback_token():
#     print("token", type(request.args.get('code')))
#     return 'ok'

if __name__ == '__main__':
    app.run()
