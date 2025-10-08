// HTML is about content. JavaScript is about behavior.
// Usually they should be in separate files.

//--------------------Variables--------------------
// let can change. const cannot change.
// Types of variables:
// - primitive types
//    - number
//    - string
//    - boolean
//    - undefined
//    - null
// - reference types
//    - object
//    - array
//    - function
let age = 21;
const lname = 'Wright';


//--------------------Objects--------------------
// Object literal defined with curly braces
let person = {
    fname: 'Ben',
    lname: lname,
    age: 21
}
// Dot notation
person.fname = 'Sarah';
// Bracket notation
person['lname'] = 'Lee';

console.log(person);


//--------------------Arrays--------------------
// Define with brackets.
// Data structure used to store lists of items
// Length and types of objects are dynamic.
// Array is an object. Keys = numbers. Values = whatever.
let selectedColors = ['red', 'blue'];
selectedColors[4] = 'yellow';
console.log(selectedColors);
// insertions/deletion methods
// pop(): remove last element
// push(): add element(s) to 
// shift(): remove first element
// unshift(): add element(s) to the start
// splice(i, j, elements): insert and remove elements at index i. Remove j items.
selectedColors.splice(2, 2, 'green', 'orange');
console.log(selectedColors);

// slice(start, end): used to create a subarray from [start, end). Also used for strings.
let favoriteColors = selectedColors.slice(1,3);
console.log(`favorite colors: ${favoriteColors}`);
for (let i=0; i<favoriteColors.length; i++) {
    console.log(favoriteColors[i]);
}


//--------------------Functions--------------------
// no need to specify types for paremeters
// or a return type for the function.
// normally, functions should precede the main code so they are loaded in memory when they are invoked.

// Log a greeting to the console.
function greet(name) {
    console.log(`Hello ${name}`);
    console.log(`The first letter of your name is: ${name.charAt(0).toUpperCase()}`);
}

// Make field yellow on focus.
function makeFieldYellow(fieldId) {
    document.getElementById(fieldId).style.backgroundColor = 'lightyellow';
}

// Make field white on blur.
function makeFieldWhite(fieldId) {
    document.getElementById(fieldId).style.backgroundColor = 'white';
}


// Check for invalid fields when the form is submitted.
// Don't submit the form (return false) and alert the user.
function validateForm() {
    let errorStr = "";

    if (!isEmailValid()) {
        errorStr += "\n- email";
    }
    if (!isZipValid()) {
        errorStr += "\n- zip";
    }

    if (errorStr.length > 0) {
        alert("The following fields are not valid: " + errorStr + "\n\nPlease correct before submitting.");
        return false;
    }
}
function isEmailValid() {
    let emailEntered = document.getElementById('email').value;

    // no spaces or consecutive periods allowed
    if (emailEntered.indexOf(" ") !== -1 || emailEntered.indexOf("..") !== -1 ) {
        return false;
    }
    // one & only one @ sign allowed
    let numAts = emailEntered.split("@").length - 1;
    if (numAts !== 1) {
        return false;
    }

    return true;
}
function isZipValid() {
    let zipEntered = document.getElementById('zip').value;

    // length 5
    if (zipEntered.length !== 5) {
        return false;
    }
    // can only contain numbers
    for (let i=0; i<zipEntered.length; i++) {
        let digit = parseInt(zipEntered.charAt(i));
        if (isNaN(digit)) {
            return false;
        }
    }

    return true;
}

// When the user enters a zip code, auto-fill the city.
function fillInCity() {
    let cityName = "";
    let zipEntered = document.getElementById("zip").value;
    switch (zipEntered) {
        case "20175" :
            cityName = "Leesburg";
            break;
        case "23606" :
            cityName = "Newport News";
            break;
    }

    document.getElementById("city").value = cityName;
}

// Expand the paragraph on lorises upon click.
function expandLoris() {
    let newText = "Slow lorises are a groups of several species of " + 
        "strepsirrhine primates which make up the genus Nyctivebus. " + 
        "They have a round head, narrow snout, large eyes, and a variety " +
        "of distinctive coloration patterns that are species-dependent";
    let paragraph = document.getElementById("loris");
    paragraph.innerHTML = newText;
}

// Create a list of lorises upon click.
function createLorisList() {
    let newList = "<ul><li>Slow loris</li><li>Fast loris</li></ul>";
    document.getElementById("loris-list").innerHTML = newList;
}

// Hide an image.
function vanish(picId) {
    document.getElementById(picId).className = "hidden";
}

// Swamp image with specified newPic
function swapPic(picId, newPic) {
    document.getElementById(picId).src = newPic;
}


// Event handling.
// With functions to handle events, let's assign these functions to some HTML elements.
document.getElementById("loris-paragraph-link").onclick = expandLoris;