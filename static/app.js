// Clear the input and result boxes
function clearFields() {
    document.getElementById('text-input').value = '';  // Clear the text input
    document.getElementById('result-box').textContent = 'Encoding: ';  // Reset result box
    document.getElementById('confidence-box').textContent = 'Confidence: ';  // Reset confidence box
}

// Add event listener for the clear button
document.getElementById('clear-btn').addEventListener('click', clearFields);

document.getElementById('detect-btn').addEventListener('click', classifyText);

function classifyText() {
    const inputText = document.getElementById('text-input').value;

    fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'text-input': inputText })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Handle the response data
        const resultBox = document.getElementById('result-box');
        const encoding = data.result;
        resultBox.innerHTML = '<span class="small-text">Your input is: </span><span class="' + (encoding === 'Unicode' ? 'unicode' : 'zawgyi') + '">' + encoding + '</span>';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result-box').textContent = 'Error: ' + error.message;
    });
}
