import spotipy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from app.ml import sp
from app.models import engine, Artist, Track, db_url
import sqlite3
import json
import datetime

Session = sessionmaker(bind=engine, autoflush=False)
sess = Session()

def add_update_db(url):
    track_id = url[-22:]
    track_uri = str("spotify:track:") + track_id
    search = sp.track(track_uri)
    track_name = search['name']
    track_popularity = search['popularity']
    duration = search['duration_ms']
    explicit = search['explicit']
    release_date = search['album']['release_date']
    year = release_date[:3]

    artist_idx = search['artists'][0]['id']
    search = sp.artist(artist_idx)
    genres = json.dumps(search['genres'])
    artist_name = search['name']
    artist_uri = search['uri']
    artist_popularity = search['popularity']

    search = sp.audio_features(track_id)
    danceability = search[0]['danceability']
    energy = search[0]['energy']
    key = search[0]['key']
    loudness = search[0]['loudness']
    mode = search[0]['mode']
    speechiness = search[0]['speechiness']
    acousticness = search[0]['acousticness']
    instrumentalness = search[0]['instrumentalness']
    liveness = search[0]['liveness']
    valence = search[0]['valence']
    tempo = search[0]['tempo']

    x = Artist(id=artist_idx, name=artist_name,
                uri=artist_uri, genres=genres,
                popularity=artist_popularity)
    y = Track(id=track_id, name=track_name, uri=track_uri,
                popularity=track_popularity, duration=duration,
                explicit=explicit, release_date=release_date,
                year=year, artist_id=artist_idx, danceability=danceability,
                energy=energy, key=key, loudness=loudness, mode=mode,
                speechiness=speechiness, acousticness=acousticness,
                instrumentalness=instrumentalness, liveness=liveness,
                valence=valence, tempo=tempo)
    
    sess.merge(x)
    sess.merge(y)
    sess.commit()
