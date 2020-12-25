import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER_ID = os.environ.get("USER_ID")
USER_CLIENT = os.environ.get("USER_CLIENT")

cid = USER_ID
secret = USER_CLIENT
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
