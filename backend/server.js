const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(cors());
app.use(express.static(path.join(__dirname, "../frontend")));

const PORT = process.env.PORT || 3000;

const server = http.createServer(app);

const io = new Server(server, {
    cors: {
        origin: "http://k132vpmg7zf706ml1sw0aonr.178.105.39.91.sslip.io",
        methods: ["GET", "POST"]
    }
});

let messages = [];

io.on("connection", (socket) => {

    console.log("user connected");

    socket.emit("loadMessages", messages);

    socket.on("sendMessage", (message) => {

        messages.push(message);

        io.emit("newMessage", message);
    });

    socket.on("disconnect", () => {
        console.log("user disconnected");
    });

});

server.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});