const express = require('express'); 
const app = express();
app.use(express.json());

//  Header Middleware
const checkUsername = (req, res, next) => {
  const usernameHeader = req.get("X-Username");
  req.username = usernameHeader || null;
  next();
};


// validates data
const validateSubjects = (req, res, next) => {

  const subjects = req.body;

  if (
    !Array.isArray(subjects) ||
    !subjects.every((item) => typeof item === "string")
  ) {
    return res.status(400).send("Invalid input: expected an array of strings.");
  }
  next();
};



//  The Endpoint
app.post("/subjects", checkUsername, validateSubjects, (req, res) => {
  const { username, body: subjects } = req;

  // Handle Authentication Message
  const authPart = username
    ? `You are authenticated as ${username}.`
    : "You are not authenticated.";

  // Handle subject vs subjects
  const count = subjects.length;
  const subjectText = count === 1 ? "subject" : "subjects";

  // 3. Handle the list formatting
  const listPart = count > 0 ? `: ${subjects.join(", ")}.` : ".";

  res.send(
    `${authPart}\n\nYou have requested information about ${count} ${subjectText}${listPart}`,
  );
});



app.listen(3000, () => {
  console.log('Server is running on port 3000');
});