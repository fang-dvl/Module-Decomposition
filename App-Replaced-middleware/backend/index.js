import express from "express";
import cors from "cors";

const app = express();

app.use(express.json());
app.use(cors());

function authenticationCheck(req, res, next) {
  const username = req.header("X-Username");

  req.username = username ? username : null;
  next();
}

// function bodyMessageCheck(req, res, next) {
//   let body = req.body;

//   if (!Array.isArray(body) || !body.every((item) => typeof item === "string")) {
//     return res.status(400).json({ error: "Body must be array strings." });
//   }
//   req.bodyArray = body;
//   next();
// }

app.use(authenticationCheck);

app.post("/submit", (req, res) => {
  const bodyArray = req.body;
  const countArraySubjects = bodyArray.length;
  const arraySubjects = bodyArray.join(", ");

  const authMessage = req.username
    ? `You are authenticated as: ${req.username}`
    : `You are not authenticated`;

  const bodyMessage =
    countArraySubjects === 0
      ? `You have requested information about 0 subjects.`
      : countArraySubjects === 1
        ? `You have requested information about 1 subject: ${arraySubjects}.`
        : `You have requested information about ${countArraySubjects} subjects: ${arraySubjects}.`;

  res.send(`${authMessage}\n\n${bodyMessage}`);
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
