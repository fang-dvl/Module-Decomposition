document.addEventListener("DOMContentLoaded", () => {
  const messagesList = document.getElementById("messages-list");
  const form = document.getElementById("message-form");
  const input = document.getElementById("message-input");
  const usernameInput = document.getElementById("username-input");

  const BACKEND_URL = "https://zabihollah-namazi-chat-app-backend.hosting.codeyourfuture.io";

  async function loadMessages() {
    const res = await fetch(BACKEND_URL);
    const messages = await res.json();

    messagesList.innerHTML = "";

    messages.forEach((msg) => {
      const li = document.createElement("li");
      li.innerHTML = `
        <div><strong>${msg.username}</strong></div>
        <div>${msg.text}</div>
        <small>${msg.timeStamp}</small>
      `;
      messagesList.appendChild(li);
    });
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    await fetch(BACKEND_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: usernameInput.value,
        text: input.value,
      }),
    });

    input.value = "";
    loadMessages();
  });

  loadMessages();
  setInterval(loadMessages, 1000);
});

