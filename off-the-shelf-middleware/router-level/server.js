import express from "express";
import { StatusCodes } from "http-status-codes";

const app = express();
const router = express.Router();

const authenticate = (req, _, next) => {
  if (req.headers["x-username"]) {
    req.username = req.headers["x-username"];
  } else {
    req.username = null;
  }
  next();
};

const passRequestPostBodyAsJSONArray = (req, res, next) => {
  try {
    if (
      Array.isArray(req.body) &&
      req.body.every((item) => typeof item === "string")
    ) {
      next();
    } else {
      return res
        .status(StatusCodes.BAD_REQUEST)
        .send("Body must be an array of strings");
    }
  } catch (e) {
    res
      .status(StatusCodes.INTERNAL_SERVER_ERROR)
      .send("Something went wrong. Please try again later.");
  }
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

// middleware
app.use(express.json());
router.post("/", [authenticate, passRequestPostBodyAsJSONArray], postData);

app.use(router);

app.listen(3000, () => console.log("Server is listening at port 3000..."));
