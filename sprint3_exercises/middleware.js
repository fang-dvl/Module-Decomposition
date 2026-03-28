import express from "express";

const app = express();
const PORT = 3000;

// Middleware 1: Extract username from X-Username header
function extractUsername(req, res, next) {
  const username = req.headers["x-username"];
  req.username = username || null;
  next();
}

// Middleware 2: Parse POST body as JSON (reusable for any JSON parsing)
app.use(express.json());

// Middleware 3: Validate that body is an array of strings
function validateArrayOfStrings(req, res, next) {
  // Check if it's an array
  if (!Array.isArray(req.body)) {
    return res.status(400).send("Request body must be a JSON array");
  }

  // Check if all elements are strings
  const allStrings = req.body.every((item) => typeof item === "string");
  if (!allStrings) {
    return res.status(400).send("All array elements must be strings");
  }

  next();
}

// Apply middlewares
app.use(extractUsername);
app.post("/", validateArrayOfStrings, (req, res) => {
  const authMessage = req.username
    ? `You are authenticated as ${req.username}.`
    : "You are not authenticated.";

  const count = req.body.length;
  let subjectsMessage;
  if (count === 0) {
    subjectsMessage = "You have requested information about 0 subjects.";
  } else if (count === 1) {
    subjectsMessage = `You have requested information about 1 subject: ${req.body[0]}.`;
  } else {
    subjectsMessage = `You have requested information about ${count} subjects: ${req.body.join(
      ", "
    )}.`;
  }

  res.send(`${authMessage}\n\n${subjectsMessage}\n`);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
