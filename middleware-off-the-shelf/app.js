import express from "express";
import usernameMiddleware from "./middleware/usernameMiddleware.js";

const app = express();
app.use(express.json());

function jsonArrayValidator(req, res, next) {
  const body = req.body;

  if (!Array.isArray(body)) {
    return res.status(400).send("Bad Request: Expected a JSON array.");
  }

  const allStrings = body.every((item) => typeof item === "string");
  if (!allStrings) {
    return res
      .status(400)
      .send("Bad Request: All items in the array must be strings.");
  }
  req.subjects = body;
  next();
}

app.post("/", usernameMiddleware, jsonArrayValidator, (req, res) => {
  const username = req.username;
  const subjects = req.subjects;

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
  console.log("Off-the-shelf server is running on port 3000");
});
