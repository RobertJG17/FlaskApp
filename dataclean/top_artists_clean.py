import pandas as pd
from setup import top_artists


# ITEMS DF
def items_formatter(new, coll):
    for item in coll:
        # Converting each str item into a dictionary
        # item_dict = ast.literal_eval(item)

        # Appending dictionary as a row of information to new DataFrame
        new = new.append(item, ignore_index=True)

    return new


raw_df = pd.DataFrame(top_artists.results)

items = raw_df['items']

artists_df = pd.DataFrame()
artists_df = items_formatter(artists_df, items)

artists_df.to_html('static/top_artists.html')
