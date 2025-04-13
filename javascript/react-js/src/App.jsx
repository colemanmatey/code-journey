import { useState, useEffect } from 'react';
import './App.css'
import MovieCard from './components/MovieCard';

function App() {

	const [data, setData] = useState(null);	

	useEffect(() => {
		fetch("http://127.0.0.1:8000/data/movies/all")
			.then(res => res.json())
			.then(data => setData(data))
			.catch(error => console.error("Error fetching data:", error));
	}, []);
	

	return (
		<div>
			<h1>MovieApp</h1>
			{
				data ? 
				data.map((movie) => (
					<MovieCard movie={ movie } />
				)) :
				<p>Loading...</p>
			}
		</div>
	)
}

export default App;
