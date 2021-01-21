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
# raw_df = pd.read_html('static/top_artists.html')[0]
items_df = pd.DataFrame()
items = raw_df['items']
items_df = items_formatter(items_df, items)

# Creating labeled indices with the band names
# items_df.set_index('name', inplace=True)
items_html = items_df.to_html()
