document.getElementById("translate-btn").addEventListener("click", async () => {
  const translateBtn = document.getElementById("translate-btn");
  const source_lang = document.getElementById("input-language").value;
  const target_lang = document.getElementById("output-language").value;
  const text = document.getElementById("input-text").value.trim();

  if (!text) {
    alert("Please enter some text to translate.");
    return;
  }

  // Disable button to prevent multiple clicks
  translateBtn.disabled = true;
  translateBtn.innerText = "Translating...";

  try {
    const response = await fetch("http://127.0.0.1:5000/translate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ source_lang, target_lang, text }),
    });

    const data = await response.json();
    console.log("🔁 Response from server:", data);

    if (response.ok) {
      document.getElementById("output-text").innerText = data.translation;
    } else {
      document.getElementById("output-text").innerText = data.error || "Translation failed.";
    }
  } catch (error) {
    console.error("❌ JS Fetch Error:", error);
    document.getElementById("output-text").innerText = "⚠️ Server error. Check console.";
  } finally {
    // Re-enable button after translation is done
    translateBtn.disabled = false;
    translateBtn.innerText = "Translate";
  }
});
