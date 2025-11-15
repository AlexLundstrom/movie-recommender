import React, { useEffect, useState } from "react";

function Movie() {
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/movie/tt0468569")
      .then(res => res.json())
      .then(setMovie)
      .catch(() => setMovie(null));
  }, []);

  if (!movie) return <p>Error fetching movie</p>;

  return (
    <div>
      <h1>{movie.Title}</h1>
      <p>{movie.Plot}</p>
      {movie.Poster && movie.Poster !== "N/A" && (
        <img src={movie.Poster} alt={movie.Title} />
      )}
    </div>
  );
}

export default Movie;
