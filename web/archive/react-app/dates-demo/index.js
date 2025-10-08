dateLabel = document.getElementById("date-label");

// initialize dateLabel's text when this script loads
let today = new Date();
dateLabel.innerHTML = today;


function changeDate(dateString) {
    // unfortunately, constructing a date from dateString results in the day 
    //  being off by one. Deconstructing the string works fine.
    let parts = dateString.split("-");
    let y = Number(parts[0]);
    let m = Number(parts[1]) - 1;
    let d = Number(parts[2]);
    let newDate = new Date(y, m, d);
    dateLabel.innerHTML = newDate;
}


function decDay(dateString) {
    console.log(`Before decDay: ${dateLabel.innerHTML}`)
    let date = new Date(dateString);
    let y = date.getFullYear();
    let m = date.getMonth(); // indexed at 0, not 1
    let d = date.getDate();
    let newDate = new Date(y, m, d - 1);
    dateLabel.innerHTML = newDate;
    console.log(`After decDay: ${dateLabel.innerHTML}`)
}

function incDay(dateString) {
    console.log(`Before incDay: ${dateLabel.innerHTML}`)
    let date = new Date(dateString);
    let y = date.getFullYear();
    let m = date.getMonth(); // indexed at 0, not 1
    let d = date.getDate();
    let newDate = new Date(y, m, d + 1);
    dateLabel.innerHTML = newDate;
    console.log(`After incDay: ${dateLabel.innerHTML}`)
}
