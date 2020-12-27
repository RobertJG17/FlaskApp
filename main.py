from flask import Flask, current_app, render_template, url_for, request, redirect
import spotty
import numpy as np
import pandas as pd
import data_science_cory

app = Flask(__name__)
# df = pd.DataFrame(top_artists.results)
# cory = df.to_html('top_artists.html')
data = data_science_cory.html


@app.route('/', methods=['GET'])
def index():
    return data


@app.route('/t', methods=['GET'])
def test():
    # Allows us to return static html from folder without having to declare a variable
    return current_app.send_static_file('top_artists.html')


if __name__ == '__main__':
    app.run()
