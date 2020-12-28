import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from os.path import join, dirname
from dotenv import load_dotenv


# Pulling data from env file
dotenv_path = join(dirname(__file__), '../misc/.env')
load_dotenv(dotenv_path)

# Unique access tokens from env files
cid = os.environ.get("USER_ID")
secret = os.environ.get("USER_CLIENT")

# OAUTH FLOW (LONG TERM USAGE i.e. having user sign in to gather user information)
scope = 'user-top-read'
auth_manager = SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri="https://www.google.com/", scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) (SHORT TERM USAGE)
