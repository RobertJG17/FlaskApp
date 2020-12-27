import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from os.path import join, dirname
from dotenv import load_dotenv

scope = 'user-top-read'

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER_ID = os.environ.get("USER_ID")
USER_CLIENT = os.environ.get("USER_CLIENT")

cid = USER_ID
secret = USER_CLIENT
auth_manager=SpotifyOAuth(client_id=USER_ID, client_secret=USER_CLIENT, redirect_uri="http://127.0.0.1:5000/", scope=scope)
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
