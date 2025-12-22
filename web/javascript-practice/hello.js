/**
 * Greet user by displaying msg at console and web page.
 * @param {} name 
 */
function greet(name) {
    let fstr = `Hello, ${name}`;  // Format String
    console.log(fstr);  // Console logging
    document.getElementById("greeting-p").innerHTML = fstr;  // Adjusting inner HTML
}

/**
 * Validate form upon submission.
 * @returns  false to prevent page from reloading.
 */
function validateForm() {
    let name = document.getElementById("name").value;
    greet(name);

    // Note on returning (for an onsubmit function):
    // Usually, when a form is submitted, the page is refreshed (or a new page is 
    // loaded). If you adjust innerHTML (as this script does), your change is 
    // lost upon refresh. You can return false to prevent this.
    // Typically, a form submits a POST request to a server and navigates to a 
    // new page. So this isn't a problem 99.99% of the time.
    return false;
}