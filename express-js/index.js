// Import modules
const express = require("express");
const path = require("path");
const morgan = require("morgan");

const app = express();

// Define hostname and port
const host = "127.0.0.1";
const port = 8000;

// Set the view engine
app.set("view engine", "ejs");

// Set the views directory
app.set("views", path.join(__dirname, "views"));

// Serve static files
app.use(express.static(path.join(__dirname, "public")))

// Use a logging middleware
app.use(morgan("dev"));

// Define Routes
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
            id: 1,
            name: "John Doe",
            age: 30,
            email: "john.doe@example.com",
            occupation: "Software Engineer",
            city: "New York",
            country: "USA",
        },
        {
            id: 2,
            name: "Jane Doe",
            age: 25,
            email: "jane.doe@example.com",
            occupation: "Graphic Designer",
            city: "San Francisco",
            country: "USA",
        },
        {
            id: 3,
            name: "Jim Smith",
            age: 27,
            email: "jim.smith@example.com",
            occupation: "Product Manager",
            city: "Chicago",
            country: "USA",
        },
        {
            id: 4,
            name: "Lisa Wong",
            age: 32,
            email: "lisa.wong@example.com",
            occupation: "Data Scientist",
            city: "Seattle",
            country: "USA",
        },
        {
            id: 5,
            name: "Tom Brown",
            age: 29,
            email: "tom.brown@example.com",
            occupation: "DevOps Engineer",
            city: "Austin",
            country: "USA",
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
