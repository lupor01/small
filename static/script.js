async function analyse() {
  const text = document.querySelector("input").value;

  try {
    const response = await fetch("/sentiment", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
        "api-key": "segretissimo",
      },
      body: JSON.stringify({ text: text }),
    });

    const data = await response.json();

    document.getElementById("output").innerText =
      `Sentiment: ${data.label} (certainty: ${data.score.toFixed(2)})`;
  } catch (error) {
    document.getElementById("output").innerText = "Error: " + error.message;
  }
}
