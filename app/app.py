
from flask import Flask, request, redirect, g, render_template, session, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn import tree
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier
song_features_df = pd.read_csv("song_features.csv")
song_features_df = song_features_df.drop(["Unnamed: 0", "peak_position", "ID", "Spotify_track_id", "artist_x", "song_x"], axis=1)
#setting target and variables to look at 
target = song_features_df["hit"]
target_names = ["Yes", "No"]
#setting our data source by dropping the 
data = song_features_df.drop(["hit","hit_value"], axis=1)
feature_names = data.columns

client_id = "99ad1917d2bf4d76bb158d44ea9e7041"
secret = "1f4ac64ffd5b463cb29e1c7d25cd4cf3"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__)
app.secret_key = 'some key for session'

@app.route('/')
def student():
   return render_template('spotify.html')

#start of api thing



@app.route('/result',methods = ['POST', 'GET'])
def features():
   if request.method == 'POST':
    song_title = request.form["song_title"]
    artist_name = request.form["artist_name"]  
    track_results = sp.search(q= f'track:{song_title} artist:{artist_name}', type="track", limit=1)
    track_id = track_results["tracks"]["items"][0]["id"]
    track_features = sp.audio_features(track_id)
    df = jsonify(track_features[0]["acousticness"],track_features[0]["danceability"],track_features[0]["duration_ms"],track_features[0]["energy"],track_features[0]["instrumentalness"],track_features[0]["key"],track_features[0]["liveness"], track_features[0]["loudness"],track_features[0]["mode"],track_features[0]["speechiness"],track_features[0]["tempo"],track_features[0]["time_signature"],track_features[0]["valence"])
    #df_list = [track_features[0]["acousticness"],track_features[0]["danceability"],track_features[0]["duration_ms"],track_features[0]["energy"],track_features[0]["instrumentalness"],track_features[0]["key"],track_features[0]["liveness"], track_features[0]["loudness"],track_features[0]["mode"],track_features[0]["speechiness"],track_features[0]["tempo"],track_features[0]["time_signature"],track_features[0]["valence"]]
    #df_dict = {"acousticness": [track_features[0]["acousticness"]], "danceability": [track_features[0]["danceability"]]}
    print("Dataframe:")
    #print(type(df))
    #print(df)
    #df = pd.DataFrame(df_dict)
    #print(df_list)
    #df = df.transpose()
    #algorithm
    X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)
    rf = RandomForestClassifier(n_estimators=300)
    results = rf.fit(X_train, y_train).predict(X_test)
    rf.score(X_test, y_test)
    #new_results = rf.fit(X_train, y_train).predict(df)
    return df

#features(song_title, artist_name)

if __name__ == "__main__":
    app.run(debug=True)