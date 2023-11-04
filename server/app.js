const express = require('express');
const { exec } = require('child_process');
const bodyParser = require('body-parser');
// const spawn = require('spawn')
const app = express();
// const pythonProcess = spawn('python', ['pdfchatbot.py']);
// const pdfchatbot = require('../model')
const pythonScript = 'pdfchatbot.py';
const functionToCall = 'pdfqna';

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Define your API routes
app.get('/home', (req, res) => {
    res.send('HOME PAGE');
});

app.post('/get_response', (req, res) => {

    const parameter = 'what is hackathon?';

    exec(`python ${pythonScript} ${functionToCall} ${parameter}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }

        const pythonOutput = stdout.trim();
        console.log(`Python output: ${pythonOutput}`);
    });

    const pythonOutput = stdout.trim();
    console.log(`Python output: ${pythonOutput}`);


    if (!query) {
        return res.status(400).json({ error: 'Invalid request, query missing' });
    }

    const response = pdfchatbot(query);

    res.header('Access-Control-Allow-Origin', '*');
    res.json({ response });
});



// Start the server
const port = 5001; // Replace with your desired port number
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
