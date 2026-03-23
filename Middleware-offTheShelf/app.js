const express = require('express');
const app = express();
const PORT = 3001;

// Use Express's built-in JSON parser (off-the-shelf middleware)
app.use(express.json());

// Our custom username middleware (only one custom middleware now)
app.use((req, res, next) => {
  req.username = req.headers['x-username'] || null;
  next();
});

// POST endpoint with simple validation
app.post('/', (req, res) => {
  // Check if body is array of strings
  if (!Array.isArray(req.body)) {
    return res.status(400).send('Error: Send a JSON array');
  }
  
  for (let item of req.body) {
    if (typeof item !== 'string') {
      return res.status(400).send('Error: All items must be strings');
    }
  }
  
  const name = req.username || 'not authenticated';
  const count = req.body.length;
  const word = count === 1 ? 'subject' : 'subjects';
  const list = req.body.join(', ');
  
  res.send(`You are ${name}.\n\nYou asked about ${count} ${word}: ${list}.`);
});

app.listen(PORT, () => {
  console.log('Server started on port 3001');
});
