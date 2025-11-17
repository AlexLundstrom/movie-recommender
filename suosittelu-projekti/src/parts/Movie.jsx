import React, {useState} from "react";
import './Movie.css'

//Movie component that displays movie's details
function Movie({movie, onYes, onNo}) {
    //State to track if the movie is opened
    const[isOpened,setIsOpened]=useState(false);

    //Renders the details and buttons of the Movie component
    return (
        <div className={`movie ${isOpened ? "opened" : ""}`}>
            <h1>{movie.title}</h1>
            <h2>{movie.year}</h2>
            {isOpened && <p>{movie.plot}</p>}
            {!isOpened && (
            <>
            <button onClick={() => { setIsOpened(true); onYes(); }}>Yes</button>
            <button onClick={onNo}>No</button>
            </>
            )}
        </div>
    )
}
export default Movie;