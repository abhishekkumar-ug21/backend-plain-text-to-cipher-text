// server.js
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors"); // Import CORS
require("dotenv").config();
const cipherRoute = require("./routes/cipherRoute");

const app = express();
const PORT = process.env.PORT || 3000;

if (process.env.MODE=="pro") {
    const corsOptions = {
        origin: function (origin, callback) {
            const allowedOrigins = [
                process.env.FRONTEND_URL, //  frontend URL
                process.env.FRONTEND_URL_1, // First frontend URL
                process.env.FRONTEND_URL_2, // Second frontend URL
                process.env.FRONTEND_URL_3, // Third frontend URL
            ];
    
            // Allow requests with no origin (like mobile apps or Postman)
            if (!origin || allowedOrigins.includes(origin)) {
                callback(null, true); // Accept the request
            } else {
                callback(new Error('Not allowed by CORS')); // Reject the request
            }
        },
        // Uncomment the following lines if you want to specify methods and headers
        // methods: ["GET", "POST"], // Allowed methods
        // allowedHeaders: ["Content-Type"], // Allowed headers
    };
    
    app.use(cors(corsOptions)); // Enable CORS with options
    
}
if (process.env.MODE=="dev") {
    app.use(cors())
    
}
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
