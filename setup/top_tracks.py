from setup.config import sp

scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']

results = sp.current_user_top_tracks(time_range=ranges[2], limit=50)
