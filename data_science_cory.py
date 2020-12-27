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


# Accessing the total key in followers dict object and displaying that information in followers column
followers = df['followers'].values
follower_count = []
for follower in followers:
    follower_count.append(follower['total'])

df['followers'] = follower_count
df = df.drop(['type', 'external_urls', 'uri'], axis=1)

html = df.to_html()

