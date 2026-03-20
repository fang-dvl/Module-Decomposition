const express = require('express');
const app = express();

// middleware for  x-user header
const usernameMiddleware = (req,res,next) => {
    const usernameHeader = req.get('X-Username');
    // if exists, set if, otherwise set to null
    req.username = usernameHeader || null;
    next();
};

// middleware for body parsing and validation

app.use(express.text({ type: 'application/json'}));

const validateArrayMiddleware = (req, res, next) => {

    try {
        // attempt to parse the raw text body
        const data = JSON.parse(req.body);
        
        //check if it is an array AND every element is a string
        const isStringArray = Array.isArray(data) && data.every(item => typeof item === 'string');
         if (!isStringArray){
            return res.status(400).send("invalid input: body must be JSON array of strings");
         }

         // attach the parsed array to req.body for next handler
         req.body = data;
         next();       
    } catch (error){
        return res.status(400).send("invalid JSON format");
    }
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