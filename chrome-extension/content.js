// Example in content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === 'scrape_listing') {
        try {
            const scrapedData = scrapeAirbnbListing();
            sendResponse({ success: true, data: scrapedData });
        } catch (error) {
            console.error('Error scraping listing:', error);
            sendResponse({ success: false, error });
        }
        return true;  // Keep the message channel open until the async operation completes
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

