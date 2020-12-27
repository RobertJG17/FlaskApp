from flask import Flask, current_app, render_template, url_for, request, redirect
import spotty
import numpy as np
import pandas as pd
import data_science_cory

app = Flask(__name__)

general = data_science_cory.general_html
pop_data = data_science_cory.popular_html
top_five_genres = data_science_cory.genre_json
top_five_artists = data_science_cory.artists_json


# @app.route('/', methods=['GET'])
# def index():
#     return current_app.send_static_file('top_artists.html')
#
#
@app.route('/1', methods=['GET'])
def test():
    return general
#
#
# @app.route('/2', methods=['GET'])
# def test1():
#     return pop_data


@app.route('/top-five', methods=['GET'])
def index():
    return top_five_genres


@app.route('/top-five/artist', methods=['GET'])
def top_artists():
    return top_five_artists


if __name__ == '__main__':
    app.run()
