from flask import Flask, render_template, url_for, request, redirect
import spotty
import numpy as np
import pandas as pd
from pandas import datetime

app = Flask(__name__)


def flip_date(date):
    flipped = date.split('-')
    flipped.reverse()
    return "-".join(flipped)


def set_release_date_precision(df):
    flipped_dates = df['release_date'].apply(flip_date)
    dt_objects = pd.to_datetime(flipped_dates)
    days = dt_objects.dt.day_name()
    print(type(days))
    df['release_date_precision'] = days


def is_in_us(countries):
    return 'US' not in countries


# Reading information into a DataFrame
album_dataframe = pd.DataFrame(spotty.albums)

# Clean up the DataFrame
album_dataframe = album_dataframe.drop(['artists', 'album_group', 'album_type', 'external_urls',
                                        'href', 'id', 'images', 'type'], axis=1)

# Filter the albums that were solely a US release
us_based_albums = album_dataframe[album_dataframe['available_markets'].apply(is_in_us)]
us_based_albums.index = np.arange(len(us_based_albums))
set_release_date_precision(us_based_albums)
uba = us_based_albums.to_html()

# Setting specific day for release date precision column
set_release_date_precision(album_dataframe)

# Write DataFrame to an html file
album_output = album_dataframe.to_html()


@app.route('/', methods=['GET'])
def index():
    return album_output


@app.route('/t', methods=['GET'])
def test():
    return uba


if __name__ == '__main__':
    app.run()
