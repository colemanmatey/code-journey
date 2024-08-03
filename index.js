// Import Mongoose
const mongoose = require("mongoose");

// Import models
const User = require("./models/user");

// Load environment variables
require("dotenv").config();

// Connect to the database
const URI = process.env.DATABASE_URL;

mongoose.connect(URI)
  .then(() => {
    console.log("Connected to the Users database");
  })
  .catch((error) => {
    console.log("Error occurred during connection: " + error);
  });

// Create a MongoDB document
const user = new User({
  first_name: "Test",
  last_name: "User",
  date_of_birth: "1997-07-07",
  email: "testuser@company.com",
});

// Save the document
user.save()
  .then(() => {
    console.log("User saved to database");
    mongoose.disconnect(); // close connection after use
  })
  .catch((error) => {
    console.log("An error occurred " + error);
  });
