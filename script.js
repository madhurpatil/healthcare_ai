async function uploadAudio() {
    let file = document.getElementById("audioFile").files[0];
    let name = document.getElementById("patientName").value;

    if (!file || !name) {
        alert("Please enter patient name and upload file");
        return;
    }

    let formData = new FormData();
    formData.append("audio", file);
    formData.append("patient_name", name);

    let res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    document.getElementById("transcription").innerText = data.transcription;

    let alertBox = document.getElementById("alerts");

    if (data.emergency) {
        alertBox.innerText = "⚠️ Emergency: " + data.alerts.join(", ");
        alertBox.style.color = "red";
    } else {
        alertBox.innerText = "✅ No emergency detected";
        alertBox.style.color = "green";
    }
}