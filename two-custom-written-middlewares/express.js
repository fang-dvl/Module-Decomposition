import express from "express";

const app = express();

// Reads X-Username header and attaches it to req.username
function usernameExtractor(req, res, next) {
  const username = req.get("X-Username");
  // Attach the username to the request object (or null if not provided)
  req.username = username ? username : null;
  // Pass control to the next middleware or route
  next();
}

// Parses raw request body as JSON
function jsonBodyParser(req, res, next) {
  let data = "";

  req.on("data", (chunk) => {
    data += chunk; // collect body data
  });

  req.on("end", () => {
    try {
      const parsed = JSON.parse(data); // try to parse JSON
      req.body = parsed; // attach parsed object to req
      next();
    } catch (err) {
      res.status(400).send("Error: Invalid JSON.");
    }
  });
}

// Validates that req.body is a string array
function stringArrayValidator(req, res, next) {
  if (!Array.isArray(req.body)) {
    return res.status(400).send("Error: Body must be a JSON array.");
  }

  const allStrings = req.body.every((item) => typeof item === "string");
  if (!allStrings) {
    return res
      .status(400)
      .send("Error: Array must contain only string elements.");
  }

  next();
}

// Applies the first middleware to all routes
app.use(usernameExtractor);

// Handles POST requests and builds response message
app.post("/", jsonBodyParser, stringArrayValidator, (req, res) => {
  const username = req.username;
  const subjects = req.body;

  const authMessage = username
    ? `You are authenticated as ${username}.`
    : "You are not authenticated.";

  // Count how many subjects were requested and join them into a list
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
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
