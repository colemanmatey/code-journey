// Arrow functions

// Passing a function as a reference
const square = function (number) {
    return number * number;
}


// Arrow syntax: 0 parameters
const pi_doubled = () => {
    // Multiply the value of PI by 2
    return 3.14 * 2;
}

// Arrow syntax: 1 parameter
const cube = number => {
    // Multiple lines of code in the body need curly braces
    return number * number * number;
}

// Arrow syntax: multiple parameters
const areaOfSquare = (length, width) => length * width; // no curly braces for one line of code in body

