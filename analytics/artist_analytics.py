from dataclean.top_artists_clean import artists_df


# HELPER FUNCTIONS
# Returns DataFrame with the top five artists along with the name and image of the band
def top_five_artists(df):
    image_list = df['images'].values
    images = []
    for image in image_list:
        images.append(image[0]['url'])

    df['images'] = images
    return df[['name', 'images', 'uri']]


# Creating top 5 artist DataFrame

# ~~~~Start~~~~ #
artists = top_five_artists(artists_df[:5])
artists = artists.transpose()
artists_json = artists.to_json()
# ~~~~End~~~~ #
