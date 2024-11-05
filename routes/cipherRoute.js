const express = require("express");
const router = express.Router();
const path = require("path");
const { spawn } = require("child_process");

router.post("/generate-cipher", (req, res) => {
    const { plainText, encryptionType } = req.body;

    // Validate input
    if (!plainText || typeof plainText !== "string") {
        return res.status(400).json({ error: "Invalid input. Please provide a valid plainText." });
    }

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
        case "Caesar": // Explicitly check for Caesar if needed
            scriptPath = path.join(__dirname, "../scripts/caesar_cipher.py");
            break;
        case "Playfair": 
            scriptPath = path.join(__dirname, "../scripts/Playfair_cipher.py");
            break;
        default:
            // Default to Caesar Cipher if no valid encryption type is provided
            scriptPath = path.join(__dirname, "../scripts/cipher_script.py");
            break;
    }

    // Spawn a Python process to run the appropriate cipher script
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
