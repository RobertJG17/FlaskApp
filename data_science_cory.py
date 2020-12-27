import pandas as pd
import ast

# Reading in HTML file and formatting to a DataFrame
cory = pd.read_html('static/top_artists.html')[0]

# Initializing a new DataFrame
df = pd.DataFrame()

# Grabbing items column from OG DataFrame
items = cory['items']

for item in items:
    # Converting each str item into a dictionary
    item_dict = ast.literal_eval(item)

    # Appending dictionary as a row of information to new DataFrame
    df = df.append(item_dict, ignore_index=True)

# Creating labeled indices with the band names
df = df.set_index('name')

html = df.to_html()

