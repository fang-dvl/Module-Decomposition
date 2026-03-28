import express from "express";

const app = express();

// Built-in middleware to parse JSON bodies
app.use(express.json());

//extract username from header
const extractUsername = (req, res, next) => {
  const usernameHeader = req.headers["x-username"];
  req.username = usernameHeader ? usernameHeader : null;
  next();
};

// validate JSON array from POST body
const validateJsonArray = (req, res, next) => {
  if (!Array.isArray(req.body)) {
    return res.status(400).send("Expected a JSON array.");
  }

  const allStrings = req.body.every((item) => typeof item === "string");
  if (!allStrings) {
    return res.status(400).send("Array must contain only strings.");
  }

  next();
};

// Use the middlewares
app.use(extractUsername);
app.use(validateJsonArray);

// Route handler
app.post("/", (req, res) => {
  const messages = [];

  messages.push(
    req.username
      ? `You are authenticated as ${req.username}.`
      : "You are not authenticated."
  );

  if (req.body.length > 0) {
    messages.push(
      `You have requested information about ${req.body.length} subject${
        req.body.length > 1 ? "s" : ""
      }: ${req.body.join(", ")}.`
    );
  } else {
    messages.push("You have requested information about 0 subjects.");
  }

  res.send(messages.join("\n\n"));
});

// Start server
app.listen(3000, () => {
  console.log("Server running on port 3000");
});
