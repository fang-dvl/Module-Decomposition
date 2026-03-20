const express = require("express");
const extractUsername = require("./middleware/extractUsername");
const validateJsonArray = require("./middleware/validateJsonArray");

const app = express();

app.use(express.json());

app.post(
	"/subjects",
	extractUsername,
	validateJsonArray,
	(req, res) => {
		const auth = req.username
			? `You are authenticated as ${req.username}.`
			: "You are not authenticated.";

		res.send(auth);
	}
);

module.exports = app;
