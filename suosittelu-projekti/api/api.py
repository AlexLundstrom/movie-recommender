import time
from flask import Flask, jsonify
from flask_cors import CORS
import json
import http.client
import sqlite3
import requests

app = Flask(__name__)
CORS(app)

API_KEY=""

movie_ids=["tt0111161",
"tt0068646",
"tt0071562",
"tt0468569",
"tt0050083",
"tt0108052",
"tt0167260",
"tt0110912",
"tt0060196"]

conn=sqlite3.connect("movies.db",check_same_thread=False)
cur=conn.cursor()

@app.route("/movie/<id>")
def get_movie(id):
    cur.execute("SELECT imdb_id, title, year, genre, plot FROM movies WHERE imdb_id=?", (id,))
    row=cur.fetchone()

    if row is None:
        return jsonify({"error": "Movie not found"}), 404

    movie_data={
        "imdb_id": row[0],
        "title": row[1],
        "year": row[2],
        "genre": row[3],
        "plot": row[4],
    }

    return jsonify(movie_data)

@app.route("/debug")
def debug():
    cur.execute("SELECT * FROM movies")
    return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(debug=True)