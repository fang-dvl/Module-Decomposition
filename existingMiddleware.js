const express = require("express");
const app = express();

// Use built-in JSON middleware 
app.use(express.json()); // Read the request body, parses it as JSON, automatically sets req.body, rejects invalid JSON with 400

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
 * Middleware 2 (validation only):
 * Ensure body is an array of strings
 */

// We still need to validate the shape of the data
const validateStringArrayBody = (req, res, next) => {
  if (!Array.isArray(req.body)) {
    return res.status(400).send("Request body must be a JSON array");
  }

  if (!req.body.every(item => typeof item === "string")) {
    return res.status(400).send("Array must contain only strings");
  }

  next();

};

/**
 * POST endpoint
 */



app.post(
  "/",
  usernameMiddleware,
  validateStringArrayBody,
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
