document.getElementById("applicationForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        course: document.getElementById("course").value
    };

    const response = await fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    const messageEl = document.getElementById("message");
    messageEl.innerText = result.message;
    messageEl.style.display = "block";
    messageEl.classList.add("success");
    
    // Hide form and reset after 3 seconds
    setTimeout(() => {
        document.getElementById("applicationForm").reset();
        messageEl.style.display = "none";
        messageEl.classList.remove("success");
    }, 3000);
});