from flask import Flask, current_app
from analytics import items_html, popular_html, genre_json, artists_json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('top_artists.html')


@app.route('/items', methods=['GET'])
def items():
    return items_html


@app.route('/popular', methods=['GET'])
def popular():
    return popular_html


@app.route('/genres', methods=['GET'])
def genres():
    return genre_json


@app.route('/artists', methods=['GET'])
def artists():
    return artists_json


if __name__ == '__main__':
    app.run()
