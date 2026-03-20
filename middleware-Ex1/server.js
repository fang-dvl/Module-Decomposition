const express = require("express");

const app = express();
const PORT = 3000;

// Add middlewares here
function usernameMiddleware(req, res, next) {
  const headerValue = req.header("X-Username"); // Express helper for headers
  req.username = headerValue ? headerValue : null;
  next();
}

function jsonArrayBodyMiddleware(req, res, next) {
  // Collect the raw body text
  let raw = "";

  req.on("data", (chunk) => {
    raw += chunk.toString("utf8");
  });

  req.on("end", () => {
    let parsed;

    try {
      parsed = JSON.parse(raw);
    } catch (err) {
      return res
        .status(400)
        .type("text")
        .send("Invalid JSON body. Expected a JSON array of strings.");
    }

    // Must be a JSON array
    if (!Array.isArray(parsed)) {
      return res
        .status(400)
        .type("text")
        .send("Invalid body. Expected a JSON array of strings.");
    }

    // Must contain only strings
    const allStrings = parsed.every((x) => typeof x === "string");
    if (!allStrings) {
      return res
        .status(400)
        .type("text")
        .send("Invalid body. Array must contain only strings.");
    }

    // Attach to req
    req.body = parsed;
    next();
  });

  req.on("error", () => {
    return res.status(400).type("text").send("Error reading request body.");
  });
}

app.post("/", usernameMiddleware, jsonArrayBodyMiddleware, (req, res) => {
  // Use data added by middlewares like so: req.username and req.body
  const username = req.username;

  const authLine = username
    ? `You are authenticated as ${username}.`
    : `You are not authenticated.`;

  const subjects = req.body; // should be an array of strings
  const count = subjects.length;

  let subjectsLine = `You have requested information about ${count} subject${count === 1 ? "" : "s"}`;

  if (count > 0) {
    subjectsLine += `: ${subjects.join(", ")}.`;
  } else {
    subjectsLine += `.`;
  }

  res.type("text").send(`${authLine}\n\n${subjectsLine}`);
});

app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT}`);
});
