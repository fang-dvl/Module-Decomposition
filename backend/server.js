const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(cors());

app.use(express.static(path.join(__dirname, "../frontend")));

const server = http.createServer(app);

const io = new Server(server, {
    cors: {
        origin: "*"
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

server.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});