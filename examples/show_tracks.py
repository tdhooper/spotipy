'''
    usage: show_tracks.py path_of_ids

    given a list of track IDs show the artist and track name
'''
from __future__ import print_function
import sys
import spotipy

if __name__ == '__main__':
    max_tracks_per_call = 50
    if len(sys.argv) > 1:
        file = open(sys.argv[1])
    else:
        file = sys.stdin
    tids = file.read().split()

    sp = spotipy.Spotify()
    for start in xrange(0, len(tids), max_tracks_per_call):
        results = sp.tracks(tids[start: start + max_tracks_per_call])
        for track in results['tracks']:
            print(track['name'] + ' - ' + track['artists'][0]['name'])



