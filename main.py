from flask import Flask, render_template, url_for, request, redirect
import top_artists
import spotty
import numpy as np
import pandas as pd
from pandas import datetime

app = Flask(__name__)
df = pd.DataFrame(top_artists.results)
cory = df.to_html('top-artists.html')


@app.route('/', methods=['GET'])
def index():
    return 't'


@app.route('/t', methods=['GET'])
def test():
    return cory


if __name__ == '__main__':
    app.run()
