import express from "express";
import usernameMiddleware from "./middleware/usernameMiddleware.js";
import jsonArrayMiddleware from "./middleware/jsonArrayMiddleware.js";

const app = express();

// POST route using both the JSON body parser and the username middleware
app.post("/", usernameMiddleware, jsonArrayMiddleware, (req, res) => {
  const username = req.username;
  const subjects = req.jsonArray;

  const authMessage = username
    ? `You are authenticated as ${username}!`
    : "You are not authenticated.";

  const count = subjects.length;
  const list = subjects.join(", ");

  let subjectMessage;
  if (count === 0) {
    subjectMessage = "You have no subjects.";
  } else if (count === 1) {
    subjectMessage = `You have 1 subject: ${list}.`;
  } else {
    subjectMessage = `You have ${count} subjects: ${list}.`;
  }
  res.send(`${authMessage} ${subjectMessage}`);
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
