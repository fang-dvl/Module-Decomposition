const express = require('express'); 
const app = express();

// 1. Header Middleware
const checkUsername = (req, res, next) => {
  const usernameHeader = req.get("X-Username");
  req.username = usernameHeader || null;
  next();
};

// 2. Body Parser Middleware
const ensureJsonStringArray = (req, res, next) => {
  let rawBody = "";

  req.on("data", (chunk) => {
    rawBody += chunk;
  });

  req.on("end", () => {
    let parsed;

    try {
      parsed = JSON.parse(rawBody);
    } catch {
      return res.status(400).send("Request body must be valid JSON");
    }

    if (!Array.isArray(parsed)) {
      return res.status(400).send("Request body must be a JSON array");
    }

    if (!parsed.every((item) => typeof item === "string")) {
      return res.status(400).send("Array must contain only strings");
    }

    req.body = parsed;
    next();
  });
};



// 3. The Endpoint
app.post("/subjects", checkUsername, ensureJsonStringArray, (req, res) => {
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