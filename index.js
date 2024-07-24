// Import express
const express = require("express");
const app = express();

// Define hostname and port
const host = "127.0.0.1";
const port = 8000;

// Define home route
app.get("/", (req, res) => {
    res.send("<h1>Learning Express JS</h1>");
});

// Listen to port
app.listen(port, () => {
    console.log(`Starting development server at http://${host}:${port}/`);
    console.log("Quit the server with CONTROL-C.");
});
