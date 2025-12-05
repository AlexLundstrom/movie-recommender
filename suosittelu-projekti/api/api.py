import time
from flask import Flask, jsonify
from flask_cors import CORS
import json
import http.client
import sqlite3
import requests
import os
app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "movies.db")

#Connects to the movies database, and fetches every movie in it.
def get_movies_from_database():
    conn=sqlite3.connect(db_path,check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT imdb_id, title, year, genre, plot FROM movies")
    rows=cur.fetchall()
    conn.close()

    movies=[]
    for row in rows:
        movies.append({
            "imdb_id": row[0],
            "title": row[1],
            "year": row[2],
            "genre": row[3],
            "plot": row[4],

        })
    return movies

#API endpoints, that returns all movies in the database as json.
@app.route("/movies", methods=["GET"])
def get_movies():
    movies=get_movies_from_database()
    return jsonify(movies)

#Debug endpoint, now just fetches all the movies in the database.
@app.route("/debug")
def debug():
    conn = sqlite3.connect(db_path, check_same_thread=False)
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)