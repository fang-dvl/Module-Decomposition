const usernameEl = document.getElementById("username");
const subjectsEl = document.getElementById("subjects");
const responseDiv = document.getElementById("response");
const subjectForm = document.getElementById("subjectForm");

async function postSubjectInfoRequest(e) {
  e.preventDefault();
  const username = usernameEl.value.trim();
  const subjects = subjectsEl.value
    .split("\n")
    .map((s) => s.trim())
    .filter(Boolean);
  responseDiv.textContent = "Loading...";
  try {
    const res = await fetch("http://localhost:3000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(username && { "x-username": username }),
      },
      body: JSON.stringify(subjects),
    });
    const text = await res.text();
    responseDiv.textContent = text;
  } catch (err) {
    responseDiv.textContent = "Error: " + err.message;
  }
  usernameEl.value = "";
  subjectsEl.value = "";
}

subjectForm.addEventListener("submit", postSubjectInfoRequest);
