import time
from flask import Flask, jsonify
from flask_cors import CORS
import json
import http.client

app = Flask(__name__)
CORS(app)

API_KEY=""

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