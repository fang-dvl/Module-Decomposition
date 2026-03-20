/*
Removed custom middleware that manually parsed raw text bodies
Enabled Express’s built‑in JSON parser
Updated validation middleware to work with parsed JSON
Fixed curl command by switching Content-Type 
to application/json (using: curl -X POST http://localhost:3000/subjects 
-H "Content-Type: application/json"
-H "X-Username: Ahmed"
--data '["Bees"]')
*/
import express from "express";
const app = express();
app.use(express.json()); // express builtin JSON parser


// Middleware - Extracting username 

function usernameMiddleware(req, res, next){ //middleware always has three parameters. req from client, res you send back and a next function that passes controls to next middleware
    const userName = req.header("X-Username"); //getting a custom HTTP Header from the request 
    req.userName = userName || null; //if username is not presnet store null
    next(); // this passes control to the next middleware.
}


app.post("/subjects",usernameMiddleware, (req, res) => { 
    const userName = req.userName; 
    const subjects = req.body; 
    const count = subjects.length;
    const authMessage = userName ? `You are authenticated as ${userName}.` : `You are not authenticated.`;
// Subject message
  let subjectMessage;
  if (count === 0) {
    subjectMessage = "You have requested information about 0 subjects.";
  } else if (count === 1) {
    subjectMessage = `You have requested information about 1 subject: ${subjects[0]}.`;
  } else {
    subjectMessage = `You have requested information about ${count} subjects: ${subjects.join(", ")}.`;
  }

  // Send final response
  res.send(`${authMessage}\n\n${subjectMessage}`);
});

const PORT = 3000
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`)
});
