from dataclean.top_artists_clean import artists_df
import pandas as pd


# HELPER FUNCTIONS
def genre_formatter(ser):
    # Creating new series object to hold organized artist-percentage information
    # noinspection PyTypeChecker
    genre_percent = ser.apply(lambda num: str(round(num / sum(ser) * 100, 2)) + '%')
    genre_percent.sort_values(ascending=False, inplace=True)

    # Creating and Formatting DataFrame to neatly represent Info
    gen = pd.DataFrame({'Genres': genre_percent.index[:5], 'Percentage': genre_percent.values[:5]})
    gen['Genres'] = gen['Genres'].apply(str.title)
    return gen


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
genre_col = artists_df['genres'].values
initial_set = {}
genre_set = genre_series_to_set(genre_col, initial_set)

# Generate a pandas series from genre_set
genre_series = pd.Series(genre_set)

# Store the returned DataFrame
genre_df = genre_formatter(genre_series)
genre_df = genre_df.transpose()
genre_json = genre_df.to_json()
# ~~~~End~~~~ #
