document.getElementById("inputForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    const x = parseFloat(document.getElementById("x").value);
    const y = parseFloat(document.getElementById("y").value);
    const z = parseFloat(document.getElementById("z").value);

    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ x, y, z })
    });

    if (response.ok) {
        const iframe = document.querySelector("iframe");
        iframe.src = iframe.src;
    } else {
        alert("Помилка при обробці даних!");
    }
});
