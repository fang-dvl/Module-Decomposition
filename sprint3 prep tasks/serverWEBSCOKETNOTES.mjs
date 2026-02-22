import express from "express";
import cors from "cors";
import { on } from "events";
import { server as WebSocketServer } from "websocket";

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());

const server = http.createServer(app);
const webSocketServer = new WebSocketServer({ httpServer: server });

const messages = [
	{
		id: 1,
		username: "annonymous",
		msgText: "First chat message",
		timestamp: Date.now(),
	},
];

const getRecentMessages = (since) => {
	return messages.filter((msg) => msg.timestamp > since);
};

app.get("/", (req, res) => {
	res.json(messages);
});

//get recent messages polling
app.get("/messages", (req, res) => {
	//This is the problem:
	// sincetimestapm Teach your backend how to answer “since when” queries.
	const since = parseInt(req.query.since);
	if (since) {
		res.json(getRecentMessages(since));
		return;
	}
	res.json(messages);
});

//messages with long polling
const callbacksForNewMessages = [];
app.get("/long-poll", (req, res) => {
	const since = parseInt(req.query.since);
	let messagesToSend = [];

	if (since) {
		messagesToSend = getRecentMessages(since);
	}

	if (messagesToSend.length === 0) {
		callbacksForNewMessages.push((value) => res.send(value));
	} else {
		res.send(messagesToSend);
	}
});

//add msg to chat
app.post("/", (req, res) => {
	const bodyBytes = [];
	req.on("data", (chunk) => bodyBytes.push(...chunk));
	req.on("end", () => {
		const bodyString = String.fromCharCode(...bodyBytes);
		let body;
		try {
			body = JSON.parse(bodyString);
		} catch (error) {
			console.error(`Failed to parse body ${bodyString} as JSON: ${error}`);
			res.status(400).send("Expected body to be JSON.");
			return;
		}
		if (
			typeof body != "object" ||
			!("username" in body) ||
			!("msgText" in body)
		) {
			console.error(
				`Failed to extract username and message text from body: ${bodyString}`
			);
			res
				.status(400)
				.send(
					"Expected body to be a JSON object containing keys username and message text."
				);
			return;
		}

		body.msgText = body.msgText.trim().replace(/[^a-zA-Z0-9,.;:?! ]/g, "");
		body.username = body.username.trim().replace(/[^a-zA-Z0-9,.;:?! ]/g, "");

		if (!body.msgText || !body.username) {
			res.status(400).send("Please add a quote and an username.");
			return;
		}

		if (body.msgText.length > 400 || body.username.length >= 40) {
			res
				.status(400)
				.send(
					"Message text must be up to 400 chars and username must be less than 40 chars."
				);
			return;
		}

		const newId = messages.length + 1;

		const newMessage = {
			id: newId,
			msgText: body.msgText,
			username: body.username,
			timestamp: Date.now(),
		};

		messages.push(newMessage);

		while (callbacksForNewMessages.length > 0) {
			const callback = callbacksForNewMessages.pop();
			callback([newMessage]);
		}

		res.send("ok");
	});
});

app.listen(port, () => {
	console.error(`Chat server listening on port ${port}`);
});

websocket.addEventListener("open", () => {
	log("CONNECTED");
	pingInterval = setInterval(() => {
		log(`SENT: ping: ${counter}`);
		websocket.send("ping");
	}, 1000);
});

websocket.addEventListener("message", (e) => {
	log(`RECEIVED: ${e.data}: ${counter}`);
	counter++;
});

websocket.addEventListener("message", (e) => {
	const message = JSON.parse(e.data);
	log(`RECEIVED: ${message.iteration}: ${message.content}`);
	counter++;
});

websocket.addEventListener("close", () => {
	log("DISCONNECTED");
	clearInterval(pingInterval);
});
