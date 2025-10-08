// is this outdated??

// constructor function
function PlanOG(name, price) {
    // properties of the object, specific to an instance
    this.name = name;
    this.price = price;
}

// shared properties of an object
PlanOG.prototype.cancellable = true;

// methods of the object
// note the semicolon. Beause we declare it as a variable, 
// we need a semicolon.
PlanOG.prototype.calcAnnual = function() {
    return this.price * 12;
};


// using a class
class Plan {
    constructor(name, price, space, transfer, pages) {
        this.name = name;
        this.price = price;
        this.space = space,
        this.transfer = transfer;
        this.pages = pages;
    }
}

// new keyword tells Javascript to make an object
let basicPlan = new Plan("Basic", 3.99, 100, 1000, 10);
let premiumPlan = new Plan("Premium", 5.99, 500, 5000, 50);
let ultimatePlan = new PlanOG("Ultimate", 9.99);
console.log(ultimatePlan.calcAnnual());
console.log("price" in ultimatePlan);
console.log("location" in ultimatePlan);

// getting a list of properties, including properties/methods inherited via prototype.
let listOfProperties = [];
for (let prop in ultimatePlan) {
    listOfProperties.push(prop);
}
console.log(listOfProperties);


