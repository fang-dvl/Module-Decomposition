// Middleware 1 - custom middleware - looks for a header with name "X-Username"
function usernameMiddleware(request, response, next) {
  const usernameHeader = request.header("X-Username");
  request.username = usernameHeader ? usernameHeader : null;
  next();
}

const express = require("express");
const app = express();
const PORT = 3000;

app.use(usernameMiddleware);
app.use(express.json()); // Add the built-in JSON parser middleware


app.post("/", (request, response) => {
  let responseToClient1;
  if (request.username) {
    responseToClient1 = `You are authenticated as ${request.username}.`;
  } else {
    responseToClient1 = "You are not authenticated.";
  }

  const subjects = request.body || [];
  let responseToClient2;

  if (subjects.length === 0) {
    responseToClient2 = "You have requested information about 0 subjects.";
  } else {
    responseToClient2 = `You have requested information about ${subjects.length} subject${subjects.length > 1 ? 's' : ''}: ${subjects.join(', ')}.`;
  }

  response.send(`${responseToClient1}` + "\n" + `${responseToClient2}`);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
