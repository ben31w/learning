// childNodes: 
// an array of children. Every element has this property
cn = document.childNodes;
console.log("DOCUMENT CHILD NODES");
console.log(cn); // [ <!DOCTYPE html>, html ]

doctype_cn = cn[0].childNodes;
console.log("DOCTYPE CHILD NODES");
console.log(doctype_cn); // []

html_cn = cn[1].childNodes;
console.log("HTML TAG CHILD NODES");
console.log(html_cn); // [head, #text (junk whitespace), body]
                        //      ^ junk artifact (tab and/or carriage return in HTML file)

head_cn = html_cn[0].childNodes;
console.log("HEAD TAG CHILD NODES");
console.log(head_cn); // [ #text, meta, #text, title, #text ]

body_cn = html_cn[2].childNodes;
console.log("BODY TAG CHILD NODES");
console.log(body_cn); // [ #text, <!--  Practice with DOM  -->, #text, div#ca, #text, div#ny, #text, script ]

ca_cn = body_cn[3].childNodes;
console.log("CA DIV TAG CHILD NODES");
console.log(ca_cn); // [ #text, p, #text, p, #text ]

southern_ca_cn = ca_cn[1].childNodes;
console.log("SOUTHERN CA P TAG CHILD NODES");
console.log(southern_ca_cn); // [ #text ]
                            //    Southern CA is sunny.

// firstChild
// lastChild
// nextSibling
// previousSibling
// return undefined for text nodes.


// nodeType: 
// return 1 if the node is an element, 3 if the node is a #text node.
// used to filter junk artifacts.
console.log("CA node types: ")
for (let i=0; i<ca_cn.length; i++) {
    let type = ca_cn[i].nodeType;
    if (type == 1) {
        console.log("\t1... element in HTML file")
    }
    else {
        console.log("\t3... text or whitespace in HTML file");
    }
    // console.log(`\t${ca_cn[i].nodeType}`);
}


// nodeName
// returns element type in uppercase (usually)
// it's good practice to always convert to lowercase.
// <p>: P
// <div>: DIV
// etc.
// #text: text
console.log("CA node names:")
for (let i=0; i<ca_cn.length; i++) {
    console.log(`\t${ca_cn[i].nodeName}`);
}


// nodeValue
// get value of a text node.
// Note: elements (nodeType 1) have a null nodeValue.
console.log("Some node values:")
for (let i=0; i<ca_cn.length; i++) {
    // paragraph found.
    if (ca_cn[i].nodeName.toLowerCase() === 'p') {
        // parse throught the paragraph's children.
        // If a text node is found, print the text
        let children = ca_cn[i].childNodes;
        for (let j=0; j<children.length; j++) {
            if (children[j].nodeType === 3) {
                console.log(`\tText found: ${children[j].nodeValue}`);
            }
            else {
                console.log(`\tTag found: ${children[j].nodeName}`);
            }
        }
    }
}


// hasAttribute("attribute")
// return true if an element node has a given attribute

// getAttribute("attribute")
// get attribute value

// setAttribute("attribute", "value")
// set new attribute value
let target = document.getElementById("ny");
if (target.hasAttribute("style")) {
    let attVal = target.getAttribute("style");
    console.log("Old attribute: " + attVal);

    target.setAttribute("style", "font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif")
    attVal = target.getAttribute("style");
    console.log("New attribute: " + attVal);
}


// attributes
// get a list of an elements attributes.
// you can then use nodeName and nodeValue to get the attributes and values
console.log("Attributes");
let attribute_list = target.attributes;
for (let i=0; i<attribute_list.length; i++) {
    console.log(attribute_list[i]);
}
console.log("Attributes, using nodeName and nodeValue");
for (let i=0; i<attribute_list.length; i++) {
    console.log("nodeName: " + attribute_list[i].nodeName + "\tnodeValue: " + attribute_list[i].nodeValue);
}


// createElement("elementType")
// createTextNode("string")
// appendChild(textNode)
let nodeToAdd = document.createElement("p");
nodeToAdd.setAttribute("style", "font-style: italic;");

let nodeText = document.createTextNode("Hello!");
nodeToAdd.appendChild(nodeText);

let body = html_cn[2];
body.appendChild(nodeToAdd);


// insertBefore(nodeToInsert, nodeToInsertBefore)
let newParagraph = document.createElement("p");
let newText = document.createTextNode("Welcome to New York");
newParagraph.appendChild(newText);

let ny = document.getElementById("ny");
let p1 = ny.firstChild;
ny.insertBefore(newParagraph, p1);


// removeChild(nodeToRemove)
// let nodeToRemove = ny.childNodes[2];
// ny.removeChild(nodeToRemove);