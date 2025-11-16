import React, { useEffect, useState } from "react";

function Movie() {
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/movie/tt0111161")
      .then(res => res.json())
      .then(setMovie)
      .catch(() => setMovie(null));
  }, []);

  if (!movie) return <p>Error fetching movie</p>;

  return (
    <div>
      <h1>{movie.title}</h1>
      <p>{movie.plot}</p>
      <h2>{movie.year}</h2>
    </div>
  );
}

export default Movie;
