const express = require("express");
const app = express();
const PORT = 3000;

//middle 1:
function usernameMiddleware(req, res, next) {
  const username = req.header("Username");
  req.username = username ? username : null;
  next();
}

//middle 2:
function jsonArrayBodyMiddleware(req, res, next) {
  let raw = "";
  let chunks = [];

    req.on("data", (chunk) => {
    chunks.push(chunk);
    });

  req.on("end", () => {
    try {
    raw = Buffer.concat(chunks).toString("utf8");
      const parsed = JSON.parse(raw);

      if (!Array.isArray(parsed)) {
        return res
          .status(400)
          .type("text")
          .send("Invalid body. Expected a JSON array of strings.");
      }

      const allStrings = parsed.every((item) => typeof item === "string");

      if (!allStrings) {
        return res
          .status(400)
          .type("text")
          .send("Invalid body. Array must contain only strings.");
      }

      req.body = parsed;
      next();
    } catch (err) {
      return res
        .status(400)
        .type("text")
        .send("Invalid JSON body.");
    }
  });

  req.on("error", () => {
    return res.status(400).type("text").send("Error reading body.");
  });
}


//Post endpoint:

app.post(
  "/",
  usernameMiddleware,// call middle 1
  jsonArrayBodyMiddleware, // cal middle 2
  (req, res) => {
    const username = req.username;
    const subjects = req.body;
    const count = subjects.length;

    const authLine = username
      ? `You are authenticated as ${username}.`
      : `You are not authenticated.`;

    let subjectsLine = `You have requested information about ${count} subject${
      count === 1 ? "" : "s"
    }`;

    subjectsLine += count > 0 ? `: ${subjects.join(", ")}.` : `.`;

    res.type("text").send(`${authLine}\n\n${subjectsLine}`);
  }
);

app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT}`);
});