from flask import Flask, render_template, url_for, request, redirect
import spotty
import numpy as np
import pandas as pd
from pandas import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 't'


@app.route('/t', methods=['GET'])
def test():
    return 't2'


if __name__ == '__main__':
    app.run()
