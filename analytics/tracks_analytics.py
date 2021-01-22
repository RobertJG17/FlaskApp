from dataclean.top_tracks_clean import tracks_df


# Creating top 5 track DataFrame

# ~~~~Start~~~~ #
tracks = tracks_df['name'][:5]
tracks = tracks.transpose()
tracks_json = tracks.to_json()
# ~~~~End~~~~ #
