document.getElementById("tab1-header").addEventListener("click", function () {
    switchTab("tab1");
});

document.getElementById("tab2-header").addEventListener("click", function () {
    switchTab("tab2");
});

function switchTab(tabId) {
    document.querySelectorAll(".tab").forEach(tab => {
        tab.classList.remove("active");
    });
    document.getElementById(tabId).classList.add("active");

    document.querySelectorAll(".tab-header").forEach(header => {
        header.classList.remove("active");
    });
    document.getElementById(tabId + "-header").classList.add("active");
}

// Scrape and display Airbnb listing details
chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    if (chrome.runtime.lastError) {
        console.error('Error querying tabs:', chrome.runtime.lastError);
        return;
    }
    if (tabs.length === 0) {
        console.error('No active tabs found.');
        return;
    }
    chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: () => {
            try {
                const url = window.location.href;
                const match = url.match(/https:\/\/www\.airbnb\.com\/rooms\/(\d+)/);
                if (match && match[1]) {
                    const listingId = match[1];
                    sendToBackend(listingId);
                } else {
                    console.error('Unable to extract Airbnb listing ID from URL');
                }
            } catch (error) {
                console.error('Error executing script:', error);
            }
        }
    }, 
    (results) => {
            console.log('No results returned from script execution.');
    });
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

