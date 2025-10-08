// This a comment in JavaScript. The browser ignores comments.

// JavaScript adds interactivity to web pages. 
// You can do stuff in JavaScript that you can't do with basic HTML href's.


// Constants
const rightPane = document.getElementById("right-pane");


function removeAllChildNodes(parentNode) {
    while (parentNode.firstChild) {
        parentNode.removeChild(parentNode.firstChild);
    }
}


function expandState(stateName) {
    removeAllChildNodes(rightPane);

    let newImg = document.createElement("img");
    newImg.src = `images/${stateName}.jpeg`;
    newImg.width = "500";
    newImg.height = "300";

    let newPar = document.createElement("p");
    newPar.appendChild(document.createTextNode(`Welcome to ${stateName.toUpperCase()}`));

    rightPane.appendChild(newImg);
    rightPane.appendChild(newPar);
}