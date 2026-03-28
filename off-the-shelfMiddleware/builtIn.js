import express from "express";
const app = express();

const header = (req, res, next) => {
  const userNameHeader = req.header["x-username"];
  req.username = userNameHeader ? userNameHeader : null;
  next();
};
app.use(header);
app.use(express.json()); //built -in json parser

app.post("/", (req, res) => {
  const subjects = Array.isArray(req.body) ? req.body : [];

  if (!subjects.every((item) => typeof item === "string")) {
    return res.status(400).send("Expected an array of strings.");
  }

  const messages = [];
  messages.push(
    req.username
      ? `You are authenticated as ${req.username}`
      : "You are not authenticated."
  );
  messages.push(
    subjects.length > 0
      ? `You have requested information about ${
          subjects.length
        } subjects: ${subjects.join(", ")}`
      : "You have requested information about 0 subjects."
  );

  res.send(messages.join("\n\n"));
});

app.listen(3001, () => {
  console.log("Server running on port 3001 (built-in middleware version)");
});
