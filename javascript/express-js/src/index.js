import express from "express";
import cors from "cors";
import 'dotenv/config';

import execute, { getDBList, createUser, getAllMovies } from "./database.js";

const app = express();

// middleware
app.use(cors());

// routes
app.get("/", (req, res) => {
    res.send("Hello world!");
})

app.get("/db/atlas", async (req, res) => {
    await execute(getDBList);
    res.send("Data retrieved")
})

app.get("/data/movies/all", async (req, res) => {
    const movies = await execute(getAllMovies);
    res.json(movies);
})

app.get("/data/user/create", async (req, res) => {
    const user = {
        name: "Josiah Macintosh",
        email: "jmac@company.com",
        password: "32jf032rjsaf@3"
    }
    
    await execute(async (client) => await createUser(client, user));
    res.status(200).send("User successfully created!");

})

// api
app.get("/api/data", async (req, res) => {
    const url = `https://api.nasa.gov/planetary/apod?api_key=${process.env.API_KEY}`;

    try {
        const response = await fetch(url);
        const result = await response.json();
        res.json(result);
    } catch (error) {
        console.error(error);
        res.status(500).send('Failed to fetch data');
    }
})

// listen
app.listen(process.env.PORT, () => {
    console.log(`Server running on http://${process.env.HOST}:${process.env.PORT}/`)
})