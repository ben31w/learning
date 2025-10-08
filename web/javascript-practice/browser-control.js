const WIKIPEDIA = "https://en.wikipedia.org/wiki/Main_Page";

function checkForPopupBlocker() {
    let testPop = window.open(WIKIPEDIA);
    if (testPop === null || typeof(testPop) === "undefined") {
        alert("Please disable your popup blocker");
    }
    testPop.close();
}

function openWikipedia() {
    // alternative:
    // window.location.assign(WIKIPEDIA);
    window.location.href = WIKIPEDIA;
}

function openWikipediaPopup() {
    window.open(WIKIPEDIA, "wiki_window", "width=1620,height=700");
}

function refresh() {
    window.location.reload();
}

// logging :P
// for getting the url, you could omit window and href.
// or you could use document.URL
console.log("URL: " + window.location.href);
console.log("Domain: " + window.location.hostname);
console.log("Path: " + window.location.pathname);
console.log("User came from: " + document.referrer);