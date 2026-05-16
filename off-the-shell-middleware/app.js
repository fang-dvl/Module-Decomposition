import express from "express";
import usernameMiddleware from "./middleware/usernameMiddleware.js";

const app = express();

// built-in middleware
app.use(express.json());

app.post("/", usernameMiddleware, (req, res) => {
  const subjects = req.body;

  if (!Array.isArray(subjects)) {
    return res.status(400).send("Body must be a JSON array");
  }

  if (!subjects.every(item => typeof item === "string")) {
    return res.status(400).send("Array must contain only strings");
  }

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


app.listen(4001, () => {
  console.log("Server running on 4001");
});
