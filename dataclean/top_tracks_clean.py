import pandas as pd
from setup import top_tracks


# ITEMS DF
def items_formatter(new, coll):
    for item in coll:
        # Converting each str item into a dictionary
        # item_dict = ast.literal_eval(item)

        # Appending dictionary as a row of information to new DataFrame
        new = new.append(item, ignore_index=True)

    return new


# raw_df = pd.read_html('static/top_artists.html')[0]
raw_df = pd.DataFrame(top_tracks.results)

items = raw_df['items']

tracks_df = pd.DataFrame()
tracks_df = items_formatter(tracks_df, items)

tracks_df.to_html()
