const express = require("express");
const app = express();
const port = 3000;

function usernameMiddleware(req, res, next) {
  const username = req.header("X-Username");
  req.username = username || null;
  next();
}

function jsonArrayMiddleware(req, res, next) {
  let data = "";
  req.on("data", chunk => {
    data += chunk;
  });

  req.on("end", () => {
    try {
      const parsed = JSON.parse(data);
      if (!Array.isArray(parsed) || !parsed.every(item => typeof item === "string")) {
        return res.status(400).send("Invalid body: must be a JSON array of strings.");
      }
      req.body = parsed;
      next();
    } catch {
      return res.status(400).send("Invalid JSON.");
    }
  });
}

app.post("/", usernameMiddleware, jsonArrayMiddleware, (req, res) => {
  const authMessage = req.username
    ? `You are authenticated as ${req.username}.`
    : "You are not authenticated.";

  const subjects = req.body;
  const subjectCount = subjects.length;
  const subjectList = subjects.join(", ");

  const subjectMessage =
    subjectCount === 1
      ? `You have requested information about 1 subject: ${subjectList}.`
      : `You have requested information about ${subjectCount} subjects: ${subjectList}.`;

  res.send(`${authMessage}\n\n${subjectMessage}`);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
