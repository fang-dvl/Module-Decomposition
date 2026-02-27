import express from 'express';

const app = express();
const PORT = 3000;

// Parse JSON bodies(built-in)
app.use(express.json());

// Middleware1,  Extract username from header
function usernameMiddleware(req, res, next) {
  const username = req.header('X-Username');
  req.username = username || null;
  next();
}


//Reusable validator 
function validateArrayOf(type) {
  return function (req, res, next) {
    if (
      !Array.isArray(req.body) ||
      !req.body.every(item => typeof item === type)
    ) {
      return res
        .status(400)
        .send(`Invalid body: must be JSON array of ${type}s`);
    }

    next();
  };
}

// Route

app.post(
  '/info',
  usernameMiddleware,
  validateArrayOf('string'),
  (req, res) => {
    const authMessage = req.username
      ? `You are authenticated as ${req.username}.`
      : 'You are not authenticated.';

    const count = req.body.length;
    const subjects = req.body.join(', ');
    const subjectWord = count === 1 ? 'subject' : 'subjects';

    const subjectMessage = count
      ? `You have requested information about ${count} ${subjectWord}: ${subjects}.`
      : 'You have requested information about 0 subjects.';

    res.send(`${authMessage}\n\n${subjectMessage}`);
  }
);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});