import express from "express";
const app = express();

const assignHeader = (req, res, next) => {
  req.username = req.headers["x-username"] ? req.headers["x-username"] : null;
  next();
};

app.use(assignHeader);
app.use(express.json());

app.post("/", (req, res) => {
  let message = [];
  if (req.username) {
    message.push(`You are authenticated as ${req.username}`);
  } else {
    message.push("You are not authenticated.");
  }
  if (req.body.length > 0) {
    message.push(
      `You have requested information about ${
        req.body.length
      } subjects: ${req.body.join(", ")}\n`
    );
  } else {
    message.push("You have requested information about 0 subjects.\n");
  }
  res.send(message.join("\n\n"));
});

app.listen(3000, () => {
  console.error(`server listening on port 3000`);
});
