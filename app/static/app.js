document.addEventListener("DOMContentLoaded",()=>{document.querySelectorAll("[data-device-id]").forEach(control=>{control.addEventListener("change",async()=>{const deviceId=control.dataset.deviceId;const state=control.checked;try{const response=await fetch(`/api/devices/${deviceId}/power`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({state})});const result=await response.json();if(!result.ok){control.checked=!state;alert(result.error||"Could not control device.");}}catch(error){control.checked=!state;alert("Could not reach the smart-home server.");}});});});

document.addEventListener("DOMContentLoaded", () => {
    const runButton = document.getElementById("run-automations");
    const resultBox = document.getElementById("automation-result");
    if (!runButton) return;

    runButton.addEventListener("click", async () => {
        runButton.disabled = true;
        try {
            const response = await fetch("/api/automations/run", {method: "POST"});
            const result = await response.json();
            resultBox.textContent = result.ok
                ? `Executed ${result.results.length} matching rule(s).`
                : "Automation run failed.";
            setTimeout(() => window.location.reload(), 700);
        } catch (error) {
            resultBox.textContent = "Could not run automation rules.";
        } finally {
            runButton.disabled = false;
        }
    });
});
