import pandas as pd
import numpy as np
import ast


#################################
#### FORMAT HELPER FUNCTIONS ####
#################################


# BASE
def base_formatter(new, coll):
    for item in coll:
        # Converting each str item into a dictionary
        item_dict = ast.literal_eval(item)

        # Appending dictionary as a row of information to new DataFrame
        new = new.append(item_dict, ignore_index=True)

    return new


# POPULAR
def popular_formatter(pop):
    followers = pop['followers'].values
    follower_count = []
    for follower in followers:
        follower_count.append(follower['total'])

    pop['followers'] = follower_count
    pop.drop(['type', 'external_urls', 'uri'], axis=1, inplace=True)
    pop.sort_values(by='popularity', ascending=False, inplace=True)
    return pop


# GENRES
def genre_formatter(ser):
    # Creating new series object to hold organized artist-percentage information
    # noinspection PyTypeChecker
    genre_percent = ser.apply(lambda num: str(round(num / sum(ser) * 100, 2)) + '%')
    genre_percent.sort_values(ascending=False, inplace=True)

    # Creating and Formatting DataFrame to neatly represent Info
    gen = pd.DataFrame({'Genres of Choice': genre_percent.index[:5], 'Percentage': genre_percent.values[:5]})
    gen['Genres of Choice'] = gen['Genres of Choice'].apply(str.title)
    gen.index += 1
    return gen


########################################################################

####################
#### DATAFRAMES ####
####################


## GENERAL ##


# ---HELPER FUNCTIONS---
def top_five_artists(artists):
    image_list = artists['images'].values
    images = []
    for image in image_list:
        images.append(image[0]['url'])

    artists['images'] = images
    artists.index = np.arange(1, len(artists) + 1)
    return artists[['name', 'images']]


# Reading in HTML file and formatting to a DataFrame

# raw_df = pd.DataFrame(top_artists.results) (Development Ready statement)
raw_df = pd.read_html('static/top_artists.html')[0]
new_df = pd.DataFrame()
items = raw_df['items']
new_df = base_formatter(new_df, items)

# Creating top 5 artist DataFrame
artists_df = top_five_artists(new_df[:5])
artists_json = artists_df.to_json()

# Creating labeled indices with the band names
new_df.set_index('name', inplace=True)

# Writing base DataFrame to HTML file
general_html = new_df.to_html()

########################################################################


## POPULAR ##


popular = new_df
popular = popular_formatter(popular)
popular_html = popular.to_html()


########################################################################


## GENRES ##


# ---HELPER FUNCTIONS---

# Generates a list of unique genres with the corresponding # of appearances throughout the DataFrame
def genre_series_to_set(cols, st):
    for genres in cols:
        for genre in genres:
            if genre in st:
                st[genre] += 1
            else:
                st[genre] = 1
    return st


genre_col = new_df['genres'].values
initial_set = {}
genre_set = genre_series_to_set(genre_col, initial_set)

# Generate a pandas series from genre_set
genre_series = pd.Series(genre_set)

# Store the returned DataFrame
genre_df = genre_formatter(genre_series)
genre_json = genre_df.to_json()
