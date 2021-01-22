from dataclean.top_tracks_clean import tracks_df


# GENERAL #

# HELPER FUNCTIONS
# Returns DataFrame with the top five artists along with the name and image of the band

# ~~~~Start~~~~ #

# Creating top 5 artist DataFrame

tracks = tracks_df['name'][:5]
tracks = tracks.transpose()
tracks_json = tracks.to_json()
# ~~~~End~~~~ #
