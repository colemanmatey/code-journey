// Import modules
const express = require("express");
const path = require("path");

const app = express();

// Define hostname and port
const host = "127.0.0.1";
const port = 8000;

// Set the view engine
app.set("view engine", "ejs");

// Set the views directory
app.set("views", path.join(__dirname, "views"));

// Define home route
app.get("/", (req, res) => {
    res.render("index", { title: "Homepage" });
});

app.get("/about", (req, res) => {
    res.render("about", { title: "About" });
});

// Handling redirects
app.get("/about-us", (req, res) => {
    res.redirect("/about");
});

// Form handling
app.post("/guest", (req, res) => {
    const data = [
        {
            name: "John Doe",
            email: "johndoe@company.com",
            age: 30,
            isMarried: true,
        },
    ];
    res.render("guest", { title: "Guest", data: data });
});

// Handling a 404 page
app.use((req, res) => {
    res.status(404).render("404", { title: "404" });
});

// Listen to port
app.listen(port, () => {
    console.log(`Starting development server at http://${host}:${port}/`);
    console.log("Quit the server with CONTROL-C.");
});
