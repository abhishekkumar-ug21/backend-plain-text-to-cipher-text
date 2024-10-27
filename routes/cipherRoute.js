// routes/cipherRoute.js
const express = require("express");
const { spawn } = require("child_process");
const path = require("path");

const router = express.Router();

router.post("/generate-cipher", (req, res) => {
    const { plainText } = req.body;

    // Validate input
    if (!plainText || typeof plainText !== "string") {
        return res.status(400).json({ error: "Invalid input. Please provide a valid plainText." });
    }

    // Path to the Python script in the scripts folder
    const scriptPath = path.join(__dirname, "../scripts/cipher_script.py");

    // Spawn a Python process to run the cipher script
    const pythonProcess = spawn("python3", [scriptPath, plainText]);

    let cipherText = "";

    // Capture data from stdout
    pythonProcess.stdout.on("data", (data) => {
        cipherText += data.toString();
    });

    // Capture data from stderr
    pythonProcess.stderr.on("data", (data) => {
        console.error(`Python script error: ${data}`);
    });

    // Handle process close
    pythonProcess.on("close", (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: "An error occurred while processing the request." });
        }
        res.json({ cipherText });
    });
});

module.exports = router;
