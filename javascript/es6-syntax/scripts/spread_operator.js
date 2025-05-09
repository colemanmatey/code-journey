// Spread operator

// old way
const fruits = ["apple", "pear", "guava", "pawpaw", "mango"];
const vegetables = ["aubergine", "tomato", "bell pepper", "carrot"]

const produce = fruits.concat(vegetables); 
console.log(produce)


// ES6 syntax
const phones = ["Samsung Galaxy A14", "iPhone 16 Pro Max"]
const tablets = ["Samsung Galaxy Tab 9+", "iPad Pro"]

const gadgets = [...phones, "Techno M12" , ...tablets];
console.log(gadgets);