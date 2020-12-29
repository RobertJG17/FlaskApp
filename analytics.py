import pandas as pd
import numpy as np
import ast
import top_artists


################################
#### FORMAT HELPER FUNCTIONS ####
#################################


# ITEMS
def items_formatter(new, coll):
    for item in coll:
        # Converting each str item into a dictionary
        # item_dict = ast.literal_eval(item)

        # Appending dictionary as a row of information to new DataFrame
        new = new.append(item, ignore_index=True)

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
    return gen


########################################################################


####################
#### DATAFRAMES ####
####################


### GENERAL ###


# ---HELPER FUNCTIONS---

# Returns DataFrame with the top five artists along with the name and image of the band
def top_five_artists(artists):
    image_list = artists['images'].values
    images = []
    for image in image_list:
        images.append(image[0]['url'])

    artists['images'] = images
    return artists[['name', 'images', 'uri']]


# ~~~~Start~~~~ #

raw_df = pd.DataFrame(top_artists.results)
# raw_df = pd.read_html('static/top_artists.html')[0]
items_df = pd.DataFrame()
items = raw_df['items']
items_df = items_formatter(items_df, items)

# Creating top 5 artist DataFrame
artists_df = top_five_artists(items_df[:5])
artists_df = artists_df.transpose()
artists_json = artists_df.to_json()

# Creating labeled indices with the band names
items_df.set_index('name', inplace=True)

# Writing base DataFrame to HTML file
items_html = items_df.to_html()

# ~~~~End~~~~ #


########################################################################


### POPULAR ###

# ~~~~Start~~~~ #

popular = items_df
popular = popular_formatter(popular)
popular_html = popular.to_html()

# ~~~~End~~~~ #


########################################################################


### GENRES ###


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


# ~~~~Start~~~~ #

genre_col = items_df['genres'].values
initial_set = {}
genre_set = genre_series_to_set(genre_col, initial_set)

# Generate a pandas series from genre_set
genre_series = pd.Series(genre_set)

# Store the returned DataFrame
genre_df = genre_formatter(genre_series)
genre_df = genre_df.transpose()
genre_json = genre_df.to_json()

# ~~~~End~~~~ #
