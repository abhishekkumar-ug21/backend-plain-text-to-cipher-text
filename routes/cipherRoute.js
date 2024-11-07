const express = require("express");
const router = express.Router();
const path = require("path");
const { spawn } = require("child_process");
require("dotenv").config(); // Load environment variables

router.post("/generate-cipher", (req, res) => {
    const { plainText, encryptionType, key } = req.body;
    console.log("key is :",key);
    // Validate input
    if (!plainText || typeof plainText !== "string") {
        return res.status(400).json({ error: "Invalid input. Please provide a valid plainText." });
    }
    console.log(plainText, encryptionType);

    // Determine which script to use based on encryptionType
    let scriptPath;
    switch (encryptionType) {
        case "AES":
            scriptPath = path.join(__dirname, "../scripts/aes_cipher.py");
            break;
        case "RSA":
            scriptPath = path.join(__dirname, "../scripts/rsa_cipher.py");
            break;
        case "DES":
            scriptPath = path.join(__dirname, "../scripts/des_cipher.py");
            break;
        case "Caesar":
            scriptPath = path.join(__dirname, "../scripts/caesar_cipher.py");
            break;
        case "Playfair":
            scriptPath = path.join(__dirname, "../scripts/Playfair_cipher.py");
            break;
        case "Vigenere":
            scriptPath = path.join(__dirname, "../scripts/vigenere_cipher.py");
            break;
        default:
            return res.status(400).json({ error: "Invalid encryption type. Supported types: AES, RSA, DES, Caesar, Playfair." });
    }

 
    const pythonProcess = spawn("python3", [scriptPath, plainText, key]);

    let cipherText = "";

    // Capture data from stdout
    pythonProcess.stdout.on("data", (data) => {
        cipherText += data.toString();
    });

    // Capture data from stderr
    pythonProcess.stderr.on("data", (data) => {
        console.error(`Python script error: ${data.toString()}`);
    });

    // Handle process close
    pythonProcess.on("close", (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: "An error occurred while processing the request." });
        }
        console.log(`Cipher text generated:\n ${cipherText}`);
        res.json({ cipherText });
    });

    // Handle error in spawning the process
    pythonProcess.on("error", (err) => {
        console.error(`Failed to start subprocess: ${err}`);
        return res.status(500).json({ error: "Failed to start the encryption process." });
    });
});

module.exports = router;
