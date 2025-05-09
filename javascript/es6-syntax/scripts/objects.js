// Objects

const person = {
    name: "Coleman",
    walk: function() {  // regular
        console.log("Walk walk");
    }
}

const animal = {
    name: "Lion",
    legs: 4,
    makeSound() {   // ES6
        return "Roooooaaaarrrr!!!";
    },
}

console.log(animal.name);
console.log(animal["legs"])
console.log(animal.makeSound())


// Object destructuring
const citizen = {
    name: "John Doe",
    dob: "18-01-1980",
    nationality: "Ghanaian",
    placeOfBirth: "Ho",
    isMarried: true,
    isEducated: false,
    numberOfKids: 4
}

const { name, dob } = citizen; // destructure only required data
console.log(name, dob);


const { nationality: n } = citizen; // use aliases
console.log(n);