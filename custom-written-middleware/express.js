import express from "express";
const app = express();

const assignHeader = (req, res, next) => {
  req.username = req.headers["x-username"] ? req.headers["x-username"] : null;
  next();
};

const parseJSON = (req, res, next) => {
  const bodyBytes = [];
  req.on("data", (chunk) => bodyBytes.push(...chunk));
  req.on("end", () => {
    const bodyString = String.fromCharCode(...bodyBytes);
    let body;
    try {
      body = JSON.parse(bodyString);
    } catch (error) {
      console.error(`Failed to parse body ${bodyString} as JSON: ${error}`);
      res.status(400).send("Expected body to be JSON.");
      return;
    }
    if (
      !Array.isArray(body) ||
      body.some((element) => typeof element !== "string")
    ) {
      console.error(
        `Failed to extract text of the message from post body: ${bodyString}`
      );
      res.status(400).send("Expected body to be an JSON array of strings.\n");
      return;
    }
    req.body = body;

    next();
  });
};

app.use(assignHeader);
app.use(parseJSON);

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
