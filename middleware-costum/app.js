import express from "express";
import usernameMiddleware from "./middleware/usernameMiddleware.js";
import jsonArrayMiddleware from "./middleware/jsonArrayMiddleware.js";

const app = express();

app.post("/", usernameMiddleware, jsonArrayMiddleware, (req, res) => {
  const subjects = req.body;

  const auth =
    req.username
      ? `You are authenticated as ${req.username}.`
      : "You are not authenticated.";

  let message = "";

  if (subjects.length === 0) {
    message = "You have requested information about 0 subjects.";
  } else if (subjects.length === 1) {
    message = `You have requested information about 1 subject: ${subjects[0]}.`;
  } else {
    message = `You have requested information about ${subjects.length} subjects: ${subjects.join(", ")}.`;
  }

  res.send(`${auth}\n\n${message}`);
});


app.listen(4000, () => {
  console.log("Server running on 4000");
});