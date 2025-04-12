import { useState, useEffect } from 'react';
import './App.css'
import NASA from './components/NASA';

function App() {

	const [data, setData] = useState(null);	

	useEffect(() => {
		fetch("http://127.0.0.1:8000/api/data")
			.then(response => response.json())
			.then(data => setData(data))
			.catch(error => console.error("Error fetching data:", error));
	}, []);
	

	return (
		<div>
			<h1>MovieApp</h1>
			{data ? <NASA data={data} /> : <p>Loading...</p>}
		</div>
	)
}

export default App;
