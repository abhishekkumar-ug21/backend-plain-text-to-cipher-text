// server.js
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors"); // Import CORS
require("dotenv").config();
const cipherRoute = require("./routes/cipherRoute");

const app = express();
const PORT = 3000;

const corsOptions = {
    origin: process.env.FRONTEND_URL, // Use the environment variable for the frontend URL
    // methods: ["GET", "POST"], // Allowed methods
    // allowedHeaders: ["Content-Type"], // Allowed headers
};

app.use(cors(corsOptions)); // Enable CORS with options
// app.use(cors())
app.use(bodyParser.json());

// Use the cipher route
app.use("/api", cipherRoute);

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

// Greeting route
app.get("/greet", (req, res) => {
    res.json({ message: "Hello, welcome to the Cipher Text API - !" });
});
