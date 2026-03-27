const express = require("express");
const app = express();

// Custom middleware 1: extract username header
function userNameMiddleware(req, res, next) {
  const username = req.header("X-Username");
  req.username = username ? username : null;
  next();
}

// Custom middleware 2: manually parse JSON array body
function jsonArrayMiddleware(req, res, next) {
  let data = "";
  req.on("data", chunk => { data += chunk; });
  req.on("end", () => {
    try {
      const parsed = JSON.parse(data || "null");
      if (!Array.isArray(parsed)) {
        return res.status(400).send("Request body must be a JSON array.");
      }
      if (!parsed.every(item => typeof item === "string")) {
        return res.status(400).send("All array elements must be strings.");
      }
      req.body = parsed;
      next();
    } catch (err) {
      res.status(400).send("Invalid JSON.");
    }
  });
}

app.post("/", userNameMiddleware, jsonArrayMiddleware, (req, res) => {
  const username = req.username;
  const subjects = req.body || [];
  let response = "";

  if (username) response += `You are authenticated as ${username}.\n\n`;
  else response += "You are not authenticated.\n\n";

  const count = subjects.length;
  if (count === 1) response += `You have requested information about 1 subject: ${subjects[0]}.`;
  else if (count > 1) response += `You have requested information about ${count} subjects: ${subjects.join(", ")}.`;
  else response += "You have requested information about 0 subjects.";

  res.send(response);
});

app.listen(3000, () => console.log("Custom middleware app running on http://localhost:3000"));
