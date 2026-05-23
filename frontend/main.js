const socket = io(
  "http://api.ylge3zmlikef3zm52i14oo8o.178.105.39.91.sslip.io"
);

const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("sendBtn");
const messageInput = document.getElementById("message");
const usernameInput = document.getElementById("username");

function addMessage(msg) {

    const div = document.createElement("div");

    div.classList.add("message");

    div.innerHTML = `
        <strong>${msg.username}</strong>
        (${msg.time})
        <br>
        ${msg.text}
    `;

    chatBox.appendChild(div);
}

socket.on("connect", () => {
    console.log("Connected:", socket.id);
});

socket.on("loadMessages", (messages) => {

    chatBox.innerHTML = "";

    messages.forEach(addMessage);

});

socket.on("newMessage", (msg) => {

    addMessage(msg);

});

sendBtn.addEventListener("click", () => {

    const text = messageInput.value.trim();

    const username =
        usernameInput.value.trim() || "Anonymous";

    if (!text) return;

    const msg = {

        username,
        text,
        time: new Date().toLocaleTimeString()

    };

    socket.emit("sendMessage", msg);

    messageInput.value = "";
});