import express from "express";
import cors from "cors";

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(cors());

let messages = [];

app.get("/", (req, res) => {
  res.json(messages);
});

app.post("/", (req, res) => {
  const { username, text } = req.body;

  if (!username || !text) {
    return res.status(400).json({ error: "username and text required" });
  }

  messages.push({
    username,
    text,
    timeStamp: new Date().toLocaleTimeString(),
  });

  res.status(201).json({ success: true });
});

app.listen(PORT, () => {
  console.log("Server running on port 3000");
});

