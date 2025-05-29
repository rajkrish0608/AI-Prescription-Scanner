async function uploadPrescription() {
  const input = document.getElementById('prescriptionInput');
  if (!input.files.length) {
    alert('Please select a prescription image.');
    return;
  }

  const formData = new FormData();
  formData.append('file', input.files[0]);

  try {
    const response = await fetch('/upload', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    alert('Error uploading file.');
    console.error(error);
  }
}

async function submitVitals() {
  const bp = document.getElementById('bp').value;
  const sugar = document.getElementById('sugar').value;
  const weight = document.getElementById('weight').value;

  const vitals = { bp, sugar, weight };
  console.log("Sending vitals:", vitals); // 👈 Add this

  try {
    const response = await fetch('/health-check', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(vitals)
    });

    const data = await response.json();
    console.log("Advice response:", data); // 👈 Add this

    document.getElementById('warnings').innerHTML = data.warnings.map(w => `<li>${w}</li>`).join('');
    document.getElementById('tips').innerHTML = data.advice.map(a => `<li>${a}</li>`).join('');
  } catch (error) {
    alert('Error getting advice.');
    console.error(error);
  }
}
