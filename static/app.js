
// Clear the input and result boxes
function clearFields() {
    document.getElementById('text-input').value = '';  // Clear the text input
    document.getElementById('result-box').textContent = 'Encoding: ';  // Reset result box
    document.getElementById('confidence-box').textContent = 'Confidence: ';  // Reset confidence box
}

// Add event listener for the clear button
document.getElementById('clear-btn').addEventListener('click', clearFields);

document.getElementById('detect-btn').addEventListener('click', classifyText);