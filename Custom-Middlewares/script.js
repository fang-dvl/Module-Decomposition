import express from 'express';
const app = express();

// Middleware 1: Extract username from header or set to null
const usernameMiddleware = (req, res, next) => {
  const username = req.header('X-Username');
  req.username = username || null;
  next();
};

// Middleware 2: Parse JSON body and validate as array of strings
const jsonArrayBodyMiddleware = (req, res, next) => {
  let data = '';
  req.on('data', chunk => {
    data += chunk;
  });
  req.on('end', () => {
    try {
      const parsed = JSON.parse(data);
      if (
        !Array.isArray(parsed) ||
        !parsed.every(item => typeof item === 'string')
      ) {
        return res.status(400).send('Invalid body: must be JSON array of strings');
      }
      req.body = parsed;
      next();
    } catch {
      return res.status(400).send('Invalid JSON');
    }
  });
};

app.post('/info', usernameMiddleware, jsonArrayBodyMiddleware, (req, res) => {
  const authMessage = req.username
    ? `You are authenticated as ${req.username}.`
    : 'You are not authenticated.';

  const count = req.body.length;
  const subjects = req.body.join(', ');
  const subjectWord = count === 1 ? 'subject' : 'subjects';
  const subjectMessage = count
    ? `You have requested information about ${count} ${subjectWord}: ${subjects}.`
    : `You have requested information about 0 subjects.`;

  res.send(`${authMessage}\n\n${subjectMessage}`);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
