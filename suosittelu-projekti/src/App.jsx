import React, { useEffect, useState } from "react";
import Genre from './parts/Genre';
import Movie from './parts/Movie';
import './App.css';

//Component that fetches the movies from the backend
//and displays them one by one using the Movie component
function App() {

  //Tracks the current screen: genres or movies
  const [screen, setScreen] = useState("genres"); 

  //Tracks the selected genre
  const [selectedGenre, setSelectedGenre] = useState(null);

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

  //Renders the genre selection screen
  if (screen === "genres") {
    //Available genres
    const genre=["Action", "Comedy", "Drama", "Adventure"];

    return (
    <div id="root-content">
      <header className="top-nav">
      <h1 className="app-title">Choose a genre</h1>
      </header>
    
      <main className="genre-container">
      {genre.map(g => (
        <button
          key={g}
           className="genre-button"
           onClick={() => {
            setSelectedGenre(g);
            setCurrentIndex(0);
            setScreen("movies");
          }}
        >
          {g}
        </button>
      ))}
    </main>
    </div>
  );

  }

  //Renders the movie recommendation screen
  if(screen==="movies"){

    //Filters movies by selected genre
  const movies_filtered_genre = movies.filter(movie =>
  movie.genre.includes(selectedGenre)
  );

  //If movies are not yet loaded
  if (!movies_filtered_genre) {
    return <p>Loading movies...</p>;
  }

  //If there are no more movies to show
  if (currentIndex>=movies_filtered_genre.length)
  {
    return <p>No more movies.</p>;
  }   

  return (
    <div id="root-content">
      <header className="top-nav">
      <h1 className="app-title">Movie Recommender</h1>
      </header>
      <header className="selected-genre">{selectedGenre}</header>
    

    <main className="movie-container">
        <Movie
          className="movie-card"
          movie={movies_filtered_genre[currentIndex]}
          onYes={() => console.log("Open the movie.")}
          onNo={() => setCurrentIndex(currentIndex + 1)}
        />
    </main>
    </div>
  );
  }
}

export default App;
