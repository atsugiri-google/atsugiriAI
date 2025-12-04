async function sendMsg() {
  const message = document.getElementById("msg").value;

  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await res.json();
  document.getElementById("res").innerText = data.reply;
}
