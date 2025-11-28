import React, { useEffect, useState } from "react";
import Movie from './parts/Movie';
import './App.css';

//Component that fetches the movies from the backend
//and displays them one by one using the Movie component
function App() {
  //Tracks the list of movies
  const [movies, setMovies] = useState(null);

  //Tracks the index of the current movie
  const[currentIndex, setCurrentIndex] = useState(0);

  //Fetches the movies from the backend
  useEffect(() => {
    fetch("http://localhost:5000/movies")
      .then(res => res.json())
      .then(setMovies)
      .catch(() => setMovies(null));
  }, []);

  //If movies are not yet loaded
  if (!movies) {
    return <p>Loading movies...</p>;
  }

  //If there are no more movies to show
  if (currentIndex>=movies.length)
  {
    return <p>No more movies.</p>;
  } 

  //Renders the current movie using the Movie component
  return (
    <div id="root-content">
      <header className="top-nav">
      <h1 className="app-title">Movie Recommender</h1>
      </header>
    

    <main className="movie-container">
        <Movie
          className="movie-card"
          movie={movies[currentIndex]}
          onYes={() => console.log("Open the movie.")}
          onNo={() => setCurrentIndex(currentIndex + 1)}
        />
    </main>
    </div>
  );
}

export default App;
