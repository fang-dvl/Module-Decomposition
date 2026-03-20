const express = require("express");
const app = express();
const PORT = 3000;

// JSON middleware
app.use(express.json());

// Middleware 1
function usernameMiddleware(req, res, next) {
  const username = req.header("Username");
  req.username = username ? username : null;
  next();
}

app.post("/", usernameMiddleware, (req, res) => {

    // validate body manually
  if (!Array.isArray(req.body) ||
      !req.body.every((x) => typeof x === "string")) {
    return res
      .status(400)
      .type("text")
      .send("Invalid body. Expected a JSON array of strings.");
  }

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
});

app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT}`);
});
