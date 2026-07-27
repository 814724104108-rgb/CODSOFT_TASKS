function answer(correct) {
    const result = document.getElementById("result");

    if (correct) {
        result.innerHTML = "✅ Correct! Never click links from unknown or suspicious emails.";
        result.style.color = "green";
    } else {
        result.innerHTML = "❌ Incorrect! Clicking unknown links can lead to phishing attacks.";
        result.style.color = "red";
    }
}