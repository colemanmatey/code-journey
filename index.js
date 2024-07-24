// Import express
const express = require("express");
const app = express();

// Define hostname and port
const host = "127.0.0.1";
const port = 8000;

// Define home route
app.get("/", (req, res) => {
    res.sendFile("./views/index.html", { root: __dirname });
});

app.get("/about", (req, res) => {
    res.sendFile("./views/about.html", { root: __dirname });
});

// Handling redirects
app.get("/about-us", (req, res) => {
    res.redirect('/about');
})

// Listen to port
app.listen(port, () => {
    console.log(`Starting development server at http://${host}:${port}/`);
    console.log("Quit the server with CONTROL-C.");
});
