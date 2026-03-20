const express = require("express");
const extractUsername = require("./middleware/extractUsername");
const parseJsonArrayBody = require("./middleware/parseJsonArrayBody");
const app = express();

app.post("/subjects", extractUsername, parseJsonArrayBody, (req, res) => {
  const auth = req.username
    ? `You are authenticated as ${req.username}.`
    : "You are not authenticated.";

  const subjectCount = req.body.length;
  const subjectLabel = subjectCount === 1 
       ? "subject" 
       : "subjects";
  const subjectList = req.body.join(", ");
  const subjectMessage =
    subjectCount === 0
      ? "You have requested information about 0 subjects."
      : `You have requested information about ${subjectCount} ${subjectLabel}: ${subjectList}.`;

  res.send(`${auth} ${subjectMessage}`);
});

module.exports = app;
