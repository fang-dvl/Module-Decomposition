const express = require("express");
const app = express();

const PORT = 3000;

app.use(express.json());

app.listen(PORT, () => {
  console.log(`server running on http://localhost:${PORT} `);
});


function usernameMiddleware(req, res, next) {
  const username = req.get("X-Username");
  req.username = username || null;
  next();
}
function bodyMiddleware(req, res, next) {
  const body = req.body;
  if (!Array.isArray(body) || !body.every((el) => typeof el === "string")) {
    return res.status(400).send("Body must be an array of strings");
  }
  next();
}
app.post("/subjects", usernameMiddleware, bodyMiddleware, (req, res) => {
  const username = req.username;
  const subjects = req.body;

  let authMessage;

  if (username) {
    authMessage = `You are authenticated as ${username}`;
  } else {
    authMessage = `You are not authenticated.`;
  }
  let countSubject = subjects.length;

  let subjectsText;
  if (countSubject === 1) {
    subjectsText = "subject";
  } else {
    subjectsText = "subjects";
  }

  let subjectList;
  if (countSubject > 0) {
    subjectList = `: ${subjects.join(", ")}`;
  } else {
    subjectList = "";
  }
  res.send(
    `${authMessage}\n\nYou have requested information about ${countSubject} ${subjectsText}${subjectList}.`
  );
});
