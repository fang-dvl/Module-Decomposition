const express = require('express');
const app = express();
const PORT = 3000;

// Middleware function to get the username from the request headers
function checkUsernameMiddleware(req, res, next) {
    // get the value of the "x-username" header from the request
    const username = req.headers['x-username'];
    // If a username is found, save it in the request object. if not found, set it to null
    req.username = username || null;
    // Built-in function that moves to the next middleware or route handler
    next();
}

// Middleware function to check if the POST body is a JSON array of strings
function checkSubjectFormatMiddleware(req, res, next) {
    let requestBody = '';

    // Collect data chunks from request body 
    req.on('data', (chunk) => {
        requestBody += chunk;
    });

    // When all data is received
    req.on('end', () => {
        try {
            // Convert requestBody to a JS object
            const parsedBody = JSON.parse(requestBody);

            // Check if parsedBody is an array and every item is a string. But if it is not, send status error message and break
            if (!Array.isArray(parsedBody) || !parsedBody.every(item => typeof item === 'string')) {
                return res.status(400).send('Error. Invalid body! Must be an array of strings');
            }
            // If valid, save parsedBody to req.body
            req.body = parsedBody;
            next();
            // If JSON is invalid, send error status message
        } catch (err) {
            res.status(400).send('Invalid JSON.');
        }
    });
}

// Run this function when someone sends a post request to "/"
app.post('/', checkUsernameMiddleware, checkSubjectFormatMiddleware, (req, res) => {
    // Get the username set by the first middleware
    const authenticatedUser = req.username;
    // Get the list of subjects set by the second middleware
    const requestedSubjects = req.body;
    // Message for the login status
    const userAuthMessage = authenticatedUser
        ? `You are authenticated as ${authenticatedUser}.`
        : 'You are not authenticated.';
    // Length of the requested subjects
    const subjectAmount = requestedSubjects.length;
    // Create string with all requested subjects
    const allSubjects = subjectAmount > 0 ? `: ${requestedSubjects.join(', ')}` : '';

    // Send the response message
    res.send(
        `${userAuthMessage}\n\nYou have requested information about ${subjectAmount} subject${
            subjectAmount !== 1 ? 's' : ''
        }${allSubjects}.`
    );
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
