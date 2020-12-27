# import spotipy
# import config

# spotty_cred = config.client_credentials_manager
# birdy_uri = 'spotify:artist:0NTSMFFapnyZfvmCwzcYPd'
# spotify = spotipy.Spotify(client_credentials_manager=spotty_cred)

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

#for album in albums:
#    print(album['name'])
