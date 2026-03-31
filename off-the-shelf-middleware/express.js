import express from "express";

const app = express();

// Built-in Express middleware to parse JSON automatically
app.use(express.json());

// Custom middleware: Get username from header
function usernameExtractor(req, res, next) {
  const username = req.get("X-Username");
  req.username = username ? username : null;
  next();
}

app.use(usernameExtractor);

app.post("/", (req, res) => {
  const username = req.username; // from header
  const subjects = req.body; // parsed JSON from express.json()

  if (!Array.isArray(subjects)) {
    return res.status(400).send("Error: Body must be a JSON array.");
  }

  const allStrings = subjects.every((item) => typeof item === "string");
  if (!allStrings) {
    return res
      .status(400)
      .send("Error: Array must contain only string elements.");
  }

  const authMessage = username
    ? `You are authenticated as ${username}.`
    : "You are not authenticated.";

  const subjectCount = subjects.length;
  const subjectList = subjects.join(", ");

  const infoMessage =
    subjectCount === 0
      ? "You have requested information about 0 subjects."
      : `You have requested information about ${subjectCount} subject${
          subjectCount > 1 ? "s" : ""
        }: ${subjectList}.`;

  res.send(`${authMessage}\n\n${infoMessage}`);
});

// Start the server
const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
