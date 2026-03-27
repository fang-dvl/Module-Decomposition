import express from "express";
import { StatusCodes } from "http-status-codes";

const app = express();
const router = express.Router();

const authenticateUser = (req, res, next) => {
  if (req.headers["x-username"]) {
    req.username = req.headers["x-username"];
  } else {
    req.username = null;
  }
  next();
};

const passRequestPostBodyAsJSONArray = (req, res, next) => {
  let body = "";
  req.on("data", (chunk) => {
    body += chunk;
  });

  req.on("end", () => {
    try {
      const jsonBody = JSON.parse(body);
      if (
        Array.isArray(jsonBody) &&
        jsonBody.every((item) => typeof item === "string")
      ) {
        req.body = jsonBody;
        next();
      } else {
        res
          .status(StatusCodes.BAD_REQUEST)
          .send("Body must be an array of strings");
      }
    } catch (e) {
      res.status(StatusCodes.BAD_REQUEST).send("Invalid JSON format");
    }
  });

  req.on("error", () => {
    res
      .status(StatusCodes.INTERNAL_SERVER_ERROR)
      .send("Error processing request");
  });
};

const postData = (req, res) => {
  const { username } = req;
  const authMessage = username
    ? `You are authenticated as ${username}`
    : "You are not authenticated";
  const subjectsLength = req.body.length;
  const infoMsg =
    subjectsLength > 0
      ? `You have requested information about ${subjectsLength} ${
          subjectsLength > 1 ? "subjects" : "subject"
        }: ${req.body.join(", ")}`
      : "You have requested information about 0 subjects";

  res.send(`${authMessage}\n\n${infoMsg}`);
};

router.post("/", [authenticateUser, passRequestPostBodyAsJSONArray], postData);

app.use(router);

app.listen(3000, () => console.log("Server is listening at port 3000..."));
