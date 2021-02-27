#-----------------------------------------------------------#
# Comments: Work on Redirect link
# Check: https://tekore.readthedocs.io/en/stable/getting_started.html

#-----------------------------------------------------------#

import tekore as tk

client_id = 'c65f2f655ab044dcac06bbdf08ca7372'
client_secret = 'e6f73320a7fe42fa84265304165cc7db'

app_token = tk.request_client_token(client_id, client_secret)


Spotify = tk.Spotify(app_token)
album = Spotify.album('4JPguzRps3kuWDD5GS6oXr')

for track in album.tracks.items:
    print(track.track_number, track.name)
