const express = require('express');
const app = express();

app.use(express.json());

// middleware for  x-user header
const usernameMiddleware = (req,res,next) => {
    const usernameHeader = req.get('X-Username');
    // if exists, set if, otherwise set to null
    req.username = usernameHeader || null;
    next();
};

// middleware for body parsing and validation

const validateArrayMiddleware = (req, res, next) => {
    // express.json() did the parsing, so..
    const data = req.body;
    
    //check if it is an array AND every element is a string
    const isStringArray = Array.isArray(data) && data.every(item => typeof item === 'string');
        if (!isStringArray){
        return res.status(400).send("invalid input: body must be JSON array of strings");
        }
        next();       
};
 // Applying the middlewares to the POST endpoint

 app.post('/subjects', usernameMiddleware, validateArrayMiddleware, (req,res) => {
    const userText = req.username
    ? `You are authenticated as ${req.username}.`
    : "Your are not authenticated.";

    const subjectCount = req.body.length;
    const subjectList = req.body.join(', ');
    const subjectSuffix = subjectCount === 1 ? 'subject' : 'subjects';

    const subjectsText = `You have requested information about ${subjectCount} ${subjectSuffix} ${subjectCount > 0 ? ': ' + subjectList : ''}.`;

    res.send(`${userText}\n\n${subjectsText}`);
 }
);

app.listen(3000, () => console.log('server running on http://localhost:3000'));