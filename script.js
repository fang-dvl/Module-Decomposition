import express from "express"
const app = express();

app.use(express.json());

function usernameExtractor(req, res, next) {
  const username = req.get("X-Username");
  req.username = username ? username : null;
  next();
}

app.post("/", usernameExtractor,(req, res) => {
  const username = req.username;
  const subjects = req.body;
   if (!Array.isArray(subjects)) {
        return res.status(400).send("Error: Body must be a JSON array.");
    }

    const CheckAllStrings = subjects.every((e) => typeof e === "string");
  if (!CheckAllStrings) {
    return res
      .status(400)
      .send("Error: Array must contain only string elements.");
  }

  let response = username
    ? `You are authenticated as ${username}.\n`
    : `You are not authenticated.\n`;

  const count = subjects.length;
  const subjectArr = subjects.join(", ");
  if (count === 0) {
    response += "You have requested information about 0 subject.";
  } else {
    const plural = count > 1 ? "subjects" : "subject";
    response += `You have requested information about ${count} ${plural}: ${subjectArr}.`;
  }

 

  res.send(response);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});