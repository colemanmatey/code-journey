import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart } from '@fortawesome/free-solid-svg-icons'

function MovieCard({ movie }) {

    const handleClickFavorite = () => {
        alert("Hello");
    }

    return (
        <div className="movie-card">
            <div className="movie-poster">
                <img src={ movie.url } alt={ movie.title } />
                <div className="movie-overlay">
                    <button className="favorite-btn" onClick={ handleClickFavorite }>
                        <FontAwesomeIcon icon={ faHeart } />
                    </button>
                </div>
            </div>
            <div className="movie-info">
                <h3>{ movie.title }</h3>
                <p>{ movie.release_date }</p>
            </div>
        </div>
    )
}

export default MovieCard;