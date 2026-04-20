async function analyse() {
  const text = document.querySelector("input").value;
  console.log("Sending:", { text });

  try {
    const response = await fetch("/sentiment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "api-key": "x",
      },
      body: JSON.stringify({ text: text }),
    });

    const data = await response.json();

    //console.log(data);

    document.getElementById("output").innerText =
      `Sentiment: ${data.label} | certainty: ${data.score.toFixed(2)}`;
  } catch (error) {
    document.getElementById("output").innerText = "Error: " + error.message;
  }
}
