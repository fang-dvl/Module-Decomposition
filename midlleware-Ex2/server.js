const express = require("express");

const app = express();
app.use(express.json()); //built in JSON parser
const PORT = 3000;


function usernameMiddleware(req, res, next) {
  const headerValue = req.header("X-Username"); // Express helper for headers
  req.username = headerValue ? headerValue : null;
  next();
}

app.post("/", usernameMiddleware,  (req, res) => {
  // Validate: must be array of strings
  if (
    !Array.isArray(req.body) ||
    !req.body.every((x) => typeof x === "string")
  ) {
    return res
      .status(400)
      .type("text")
      .send("Invalid body. Expected a JSON array of strings.");
  }

  const username = req.username;
  const authLine = username
    ? `You are authenticated as ${username}.`
    : `You are not authenticated.`;

  const subjects = req.body; // should be an array of strings
  const count = subjects.length;

  let subjectsLine = `You have requested information about ${count} subject${count === 1 ? "" : "s"}`;
  subjectsLine += count > 0 ? `: ${subjects.join(", ")}.` : `.`;

  res.type("text").send(`${authLine}\n\n${subjectsLine}`);
});

app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT}`);
});
