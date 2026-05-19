const express = require("express");
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");

const app = express();

app.use(cors());
app.use(express.json());

const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: "*",
  },
});

// Store messages in memory
let messages = [];

// Track online users
let onlineUsers = [];

io.on("connection", (socket) => {

  // delete messages
  socket.on("delete_message", (id) => {

  // remove message from array
  messages = messages.filter(
    (msg) => msg.id !== id
  );

  // notify all clients
  io.emit("message_deleted", id);
});

  console.log("User connected");

  // Send old messages
  socket.emit("load_messages", messages);


  // USER JOIN

  socket.on("join", (username) => {
     socket.username = username;

    if (
      username && !onlineUsers.includes(username)
    ) {
      onlineUsers.push(username);
    }

    io.emit("online_users", onlineUsers);
  });


  // TYPING INDICATOR

  socket.on("typing", (username) => {
     socket.broadcast.emit(
      "typing",
      username
    );
  });


  // SEND MESSAGE

  socket.on("send_message", (message) => {
    const newMessage = {
      id: Date.now(),

      text: message.text,
      user: message.user,
      color: message.color,

      likes: 0,
      dislikes: 0,

      replyTo: message.replyTo || null,

      createdAt: new Date(),
    };


    // SCHEDULED MESSAGE

    if (message.scheduledFor) {

      const delay = new Date(message.scheduledFor) - new Date();
      
      setTimeout(() => {
        messages.push(newMessage);
         io.emit(
          "receive_message",
          newMessage
        );

      }, delay);

    } else {

      messages.push(newMessage);

      io.emit(
        "receive_message",
        newMessage
      );
    }
  });


  // LIKE MESSAGE

  socket.on("like_message", (id) => {
     const msg = messages.find( (m) => m.id === id
    );
     if (msg){
         msg.likes++; io.emit(
        "update_message",
        msg
      );
    }
  });


  // DISLIKE MESSAGE

  socket.on("dislike_message", (id) => {

    const msg = messages.find(
      (m) => m.id === id
    );

    if (msg) {

      msg.dislikes++;

      io.emit(
        "update_message",
        msg
      );
    }
  });


  // DISCONNECT

  socket.on("disconnect", () => {
    onlineUsers =
      onlineUsers.filter((user) =>user !== socket.username
      );

    io.emit( "online_users", onlineUsers
    );

    console.log("User disconnected");
  });
});

server.listen(5000, () => {
  console.log(
    "Server running on port 5000"
  );
});