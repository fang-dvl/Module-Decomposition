import express from "express";
const app = express();
app.use(express.text());

//1st Middleware - Extracting username 

function usernameMiddleware(req, res, next){ //middleware always has three parameters. req from client, res you send back and a next function that passes controls to next middleware
    const userName = req.header("X-Username"); //getting a custom HTTP Header from the request 
    req.userName = userName || null; //if username is not presnet store null
    next(); // this passes control to the next middleware.
}

//2nd Middleware - Validating JSON array body
function jsonArrayMiddleware(req, res, next){
    let data;
    try {
    data = JSON.parse(req.body);
} 
catch(err){
    return res.status(400).send("Body must be valid JSON");
}
if(!Array.isArray(data)){
    return res.status(400).send("Body must be JSON array");

}
if (!data.every(item => typeof item === "string")) { //every item in the array is a string = NOT TRUE
  return res.status(400).send("Array must contain only strings");
}
req.body = data; //store validated array
next() //allows req to continue to next middleware
}

// POST route using both middlewares
app.post("/subjects",usernameMiddleware, jsonArrayMiddleware, (req, res) => { 
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
