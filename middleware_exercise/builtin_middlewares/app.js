const express = require("express");
const app = express();

// Custom middleware: get username header
function usernameMiddleware(req, res, next) {
  const username = req.header("X-Username");
  req.username = username ? username : null;
  next();
}

// Built-in Express middleware to parse JSON
app.post("/", usernameMiddleware, express.json(), (req, res) => {
  const username = req.username;
  const subjects = req.body;

  if (!Array.isArray(subjects)) {
    return res.status(400).send("Request body must be a JSON array.");
  }
  if (!subjects.every(item => typeof item === "string")) {
    return res.status(400).send("All array elements must be strings.");
  }

  const count = subjects.length;
  let response = "";
  if (username) response += `You are authenticated as ${username}.\n\n`;
  else response += "You are not authenticated.\n\n";

  if (count === 1) response += `You have requested information about 1 subject: ${subjects[0]}.`;
  else if (count > 1) response += `You have requested information about ${count} subjects: ${subjects.join(", ")}.`;
  else response += "You have requested information about 0 subjects.";

  res.send(response);
});

app.listen(3000, () => {
  console.log("✅ Built-in middleware app running on http://localhost:3000");
});
