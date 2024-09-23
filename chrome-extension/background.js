// background.js

// Listen for when the extension icon is clicked
chrome.action.onClicked.addListener((tab) => {
    // Check if the active tab's URL is an Airbnb listing page
    if (tab.url.includes("airbnb.com/rooms")) {
        console.log("Airbnb listing detected:", tab.url);
    } else {
        console.log("Not an Airbnb listing page.");
    }
});

// Monitor when the user navigates to a new Airbnb listing and trigger actions
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url.includes('airbnb.com/rooms')) {
        console.log(" to Airbnb listing:", tab.url);
        // Optionally, you can trigger further actions or logic here.
        //sendToBackend(tab.url);
    }
});


function sendToBackend(details) {
    fetch('http://localhost:8001/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(details)
    }).then(response => response.json())
      .then(data => {
          const backendDiv = document.getElementById("backend-response");
          backendDiv.innerHTML = `<p><strong>Backend Analysis:</strong> ${data.analysis}</p>`;
      }).catch(error => console.error('Error communicating with backend:', error));
}


