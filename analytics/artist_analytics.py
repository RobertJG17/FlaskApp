from dataclean.top_artists_clean import items_df


# GENERAL #

# HELPER FUNCTIONS
# Returns DataFrame with the top five artists along with the name and image of the band
def top_five_artists(artists):
    image_list = artists['images'].values
    images = []
    for image in image_list:
        images.append(image[0]['url'])

    artists['images'] = images
    return artists[['name', 'images', 'uri']]


# ~~~~Start~~~~ #

# Creating top 5 artist DataFrame
artists_df = top_five_artists(items_df[:5])
artists_df = artists_df.transpose()
artists_json = artists_df.to_json()
# ~~~~End~~~~ #
