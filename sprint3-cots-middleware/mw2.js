const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());
app.use(addUsernameProp);

const addUsernameProp = function (req, res, next) {
	const username = req.get("X-Username");

	req.username = username ?? null;

	next();
};

app.post("/", (req, res) => {
	let responseText = "";

	if (req.username) {
		responseText += `You are authenticated as ${req.username}.<br><br>`;
	} else {
		responseText += `You are not authenticated.<br><br>`;
	}

	const subject = req.body;
	const numberOfS = subject.length === 1 ? "subject" : "subjects";
	const showSubject = subject.join(", ");
	const numOfSubj = subject.length;
	responseText += `You have requested information about ${numOfSubj} ${numberOfS}: ${showSubject}.`;

	res.send(responseText);
});

const port = 3000;
app.listen(port, () => {
	console.log(`Server running at http://localhost:${port}`);
});

// Here is the problem:

// Switch to instead the JSON middleware built in to Express.
// app.use(express.json()); instead of parseBody

// Debug why the curl command suggested in the previous exercise doesn’t work. Fix this problem by modifying the curl command.
// content-type application json not present
// -H "Content-Type: application/json"

// curl -X POST \
//   -H "Content-Type: application/json" \
//   -H "X-Username: Ahmed" \
//   -d '["Birds", "Bats", "Lizards", "Bees"]' \
//   http://localhost:3000
