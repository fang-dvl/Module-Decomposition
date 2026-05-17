const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../frontend')));

const messages = [
  {
    id: 1,
    name: 'System',
    text: 'Welcome to the chat!',
    createdAt: new Date().toISOString(),
  },
];

function makeSafeText(value) {
  return String(value || '').trim();
}

app.get('/api/messages', (req, res) => {
  res.json({ messages });
});

app.post('/api/messages', (req, res) => {
  const name = makeSafeText(req.body.name) || 'Anonymous';
  const text = makeSafeText(req.body.text);

  if (!text) {
    return res.status(400).json({ error: 'Message text is required.' });
  }

  const message = {
    id: messages.length + 1,
    name,
    text,
    createdAt: new Date().toISOString(),
  };

  messages.push(message);
  res.status(201).json({ message });
});

app.listen(PORT, () => {
  console.log(`Chat app running at http://localhost:${PORT}`);
});
