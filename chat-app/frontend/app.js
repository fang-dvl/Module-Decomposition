const API = "http://localhost:5000/messages";

async function loadMessages() {
    const res = await fetch(API);
    const data = await res.json();

    const ul = document.getElementById("messages");
    ul.innerHTML = "";

    data.forEach(m => {
        const li = document.createElement("li");
        li.textContent = `${m.username}: ${m.text}`;
        ul.appendChild(li);
    });
}

async function send() {
    const username = document.getElementById("username").value;
    const text = document.getElementById("text").value;

    await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, text })
    });

    loadMessages();
}

setInterval(loadMessages, 1000);
loadMessages();