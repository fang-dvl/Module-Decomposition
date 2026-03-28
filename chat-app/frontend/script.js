const messagesList = document.getElementById("messages-list");
const form = document.getElementById("message-form");
const input = document.getElementById("message-input");
const usernameInput = document.getElementById("username-input");

const BACKEND_URL =
  "https://xwc7hmpmk5kvt9ktptcvuuke.hosting.codeyourfuture.io";

// Fetch and display messages
async function loadMessages() {
  const response = await fetch(`${BACKEND_URL}/messages`);
  const messages = await response.json();
  messagesList.innerHTML = "";
  messages.forEach((msg) => {
    const li = document.createElement("li");
    li.innerHTML = `
    <div class="message-header">
      <span class="username"> <strong>${msg.username}</strong></span>
      <span class="timestamp">${msg.timeStamp}</span>
      </div>
      <div class="message-text">${msg.text}</div>`;
    messagesList.appendChild(li);
  });
}

// Handle form submission
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const newMessage = {
    username: usernameInput.value,
    text: input.value,
    timeStamp: new Date().toLocaleTimeString("en-US", {
      hour: "numeric",
      minute: "2-digit",
      hour12: true,
    }),
  };

  await fetch(`${BACKEND_URL}/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newMessage),
  });

  input.value = "";
  usernameInput.value = "";
  loadMessages();
});

// Refresh messages every 2 seconds
setInterval(loadMessages, 2000);
