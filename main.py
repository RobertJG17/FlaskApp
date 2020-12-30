from flask import Flask, current_app, request
from analytics import items_html, popular_html, genre_json, artists_json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": ""}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    return current_app.send_static_file('top_artists.html')


@app.route('/items', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def items():
    return items_html


@app.route('/popular', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def popular():
    return popular_html


@app.route('/genres', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def genres():
    return genre_json


@app.route('/artists', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def artists():
    return artists_json

@app.route('/token/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def callback_token():
    print("token", type(request.args.get('code')))
    return 'ok'



@app.route('/user-token', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def user_token():
    data = request.json
    f = open('.cache', 'w')
    f.write(f"{data}")
    f.close()
    return data


if __name__ == '__main__':
    app.run()
