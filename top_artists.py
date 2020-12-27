import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']

sp = config.sp
results = sp.current_user_top_artists(time_range=ranges[2], limit=50)

# for sp_range in ['short_term', 'medium_term', 'long_term']:
#     print("range:", sp_range)
#
#
#
#     for i, item in enumerate(results['items']):
#         print(i, item['name'])
#     print()
