const express = require('express');
const app = express();

app.use(express.json());

const userdata = [];
const info = [];

const getUsernameFromHeader = (req, res, next) => {
  const username = req.headers['x-username'];
  userdata.push(username);
  res.locals.username = username;
  next();
};

const checkBodyIsArray = (req, res, next) => {
  if (req.body === undefined || req.body === null) {
    res.locals.subjects = [];
    return next();
  }

  if (!Array.isArray(req.body)) {
    return res.status(400).send('Request body must be an array of subjects');
  }

  res.locals.subjects = req.body;
  next();
};

const prepareReturnValue = (req, res, next) => {
  const username = res.locals.username;
  const subjects = res.locals.subjects ?? [];

  if (subjects.length > 0) {
    info.push(...subjects);
  }

  const userInfo = `You are authenticated as ${username}`;
  const userMessage = subjects.length > 0
    ? `You have requested information about ${subjects.length} subjects: ${subjects.join(', ')}`
    : 'No subjects requested';

  console.log('req.body =', req.body);
  console.log(info);
  console.log(`
    ${userInfo}
    ${userMessage}
  `);

  res.locals.responseMessage = `Username is ${username}, Subjects: ${JSON.stringify(info)}`;
  next();
};

app.use(getUsernameFromHeader);
app.use(checkBodyIsArray);
app.use(prepareReturnValue);

app.post('/', (req, res) => {
  res.send(res.locals.responseMessage);
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
})
