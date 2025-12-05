import time
from flask import Flask, jsonify
from flask_cors import CORS
import json
import http.client
import sqlite3
import requests

app = Flask(__name__)
CORS(app)

API_KEY="95006ac4"

movie_ids=[
"tt0133093", "tt1375666", "tt0816692", "tt0083658", "tt0120915", "tt2488496", "tt1853728", "tt2911666", "tt0088763", "tt0120737", "tt0102926", "tt0110357", "tt0369610", "tt0120338", "tt0114709", "tt0118799", "tt0120586", "tt0109831", "tt0109832", "tt0109833",
"tt0078748", "tt0081505", "tt0109830", "tt0111161", "tt0093058", "tt0120815", "tt0120735", "tt0114369", "tt0110357", "tt0102926", "tt0110912", "tt0137523", "tt0109832", "tt0120586", "tt0109831", "tt0088763", "tt0120338", "tt0118799", "tt0103064", "tt0109833"
]

conn=sqlite3.connect("movies.db")
cur=conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
    imdb_id TEXT PRIMARY KEY,
    title TEXT,
    year TEXT,
    genre TEXT,
    plot TEXT
)
""")

conn.commit()

def fetch_movie(imdb_id):
    url = f"https://omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()           # raise error on bad HTTP response
        data = resp.json()                # parse JSON
    except (requests.RequestException, ValueError) as e:
        print(f"Skipping {imdb_id}: {e}")
        return None                       # skip if fetch or parse fails

    if data.get("Response") == "False":
        print(f"Skipping {imdb_id}: not found")
        return None

    return {
        "imdb_id": imdb_id,
        "title": data.get("Title"),
        "year": data.get("Year"),
        "genre": data.get("Genre"),
        "plot": data.get("Plot"),
    }

# loop through IDs
for imdb_id in movie_ids:
    movie = fetch_movie(imdb_id)
    if movie is None:
        continue  # skip this ID if fetch failed

    cur.execute("""
        INSERT OR REPLACE INTO movies (imdb_id, title, year, genre, plot)
        VALUES (?, ?, ?, ?, ?)
    """, (
        movie["imdb_id"],
        movie["title"],
        movie["year"],
        movie["genre"],
        movie["plot"]
    ))
    conn.commit()
    print(f"Saved: {movie['title']}")
    time.sleep(0.5)

conn.close()
print("Done.")

@app.route("/movie/<id>")
def get_movie(id):
    conn = http.client.HTTPSConnection("www.omdbapi.com")

    conn.request("GET", f"/?i={id}&apikey={API_KEY}")

    res = conn.getresponse()
    data = res.read()

    movie_data = json.loads(data.decode("utf-8"))
    return jsonify(movie_data)


if __name__ == "__main__":
    app.run(debug=True)