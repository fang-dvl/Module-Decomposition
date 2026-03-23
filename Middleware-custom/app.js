const express = require('express');
const app = express();
const PORT = 3000;

// Middleware 1: Check username header
app.use((req, res, next) => {
  req.username = req.headers['x-username'] || null;
  next();
});

// Middleware 2: Parse JSON and check if body is string array
app.use((req, res, next) => {
  if (req.method !== 'POST') return next();
  
  let body = '';
  req.on('data', chunk => {
    body += chunk.toString();
  });
  
  req.on('end', () => {
    try {
      req.body = JSON.parse(body);
    } catch (error) {
      return res.status(400).send('Error: Invalid JSON');
    }
    
    // Simple array check
    if (!Array.isArray(req.body)) {
      return res.status(400).send('Error: Send a JSON array');
    }
    
    // Simple string check
    for (let item of req.body) {
      if (typeof item !== 'string') {
        return res.status(400).send('Error: All items must be strings');
      }
    }
    
    req.subjects = req.body;
    next();
  });
});

// POST endpoint
app.post('/', (req, res) => {
  const name = req.username ? `authenticated as ${req.username}` : 'not authenticated';
  const count = req.subjects.length;
  const word = count === 1 ? 'subject' : 'subjects';
  const list = req.subjects.join(', ');
  
  res.send(`You are ${name}.\n\nYou asked about ${count} ${word}: ${list}.`);
});

app.listen(PORT, () => {
  console.log('Custom server started on port 3000');
});