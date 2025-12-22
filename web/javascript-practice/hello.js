// ===============
// FUNCTIONS
// ===============
/**
 * Greet user by displaying msg at console and web page.
 * @param {} name 
 */
function greet(name) {
    if (name != null) {
        let fstr = `Hello, ${name}`;  // Format String
        console.log(fstr);  // Console logging
        // Adjusting inner HTML
        document.getElementById("greeting-p").innerHTML = fstr;
    }
}


/**
 * Validate form upon submission.
 * @returns  false to prevent page from reloading.
 */
function validateForm() {
    let name = document.getElementById("name").value;
    greet(name);
}


// ===============
// EVENT LISTENERS
// ===============
document.getElementById("greeting-form").addEventListener(
    'submit', 
    function(event) {
        // Usually, when a form is submitted, the page is refreshed (or a new page 
        // is loaded). If you adjust innerHTML (as this script does), your change 
        // is lost upon refresh. Call "preventDefault" to prevent this.
        // Typically, a form submits a POST request to a server and navigates to a 
        // new page. So this isn't a problem 99.99% of the time.
        event.preventDefault();
        validateForm();
    }
);