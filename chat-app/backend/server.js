import express from "express";
import cors from "cors";

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

let messages = [];

// GET messages
app.get("/messages", (req, res) => {
    res.json(messages);
});

// POST message
app.post("/messages", (req, res) => {
    const { username, text } = req.body;

    messages.push({ username, text });

    res.json({ success: true });
});

app.listen(port, () => {
    console.log(`Backend running on http://localhost:${port}`);
});