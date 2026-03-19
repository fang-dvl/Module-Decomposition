const express = require("express");
const app = express();

/**
 * Middleware 1:
 * Read X-Username header and attach it to req.username
 */
const usernameMiddleware = (req, res, next) => {
  const username = req.header("X-Username");
  req.username = username ? username : null;
  next();
};


/**
 * Middleware 2:
 * Parse POST body as JSON array of strings
 */
const jsonArrayMiddleware = (req, res, next) => {
  let rawBody = "";

  req.on("data", chunk => {
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

    if (!parsed.every(item => typeof item === "string")) {
      return res.status(400).send("Array must contain only strings");
    }

    req.body = parsed;
    next();
  });
};



/**
 * POST endpoint
 */
app.post(
  "/",
  usernameMiddleware,
  jsonArrayMiddleware,
  (req, res) => {
    const username = req.username ?? "Anonymous";
    const subjects = req.body;

    res.send(
`You are authenticated as ${username}.

You have requested information about ${subjects.length} subjects: ${subjects.join(", ")}.`
    );
  }
);

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
