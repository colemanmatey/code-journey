// var
for (var i = 0; i < 5; i++) {
    var j = 20;
    console.log("i:", i, "j:", j);
}
console.log("Outside the loop -", "i:", i, "j:", j); // variables are accessible


// let
for (let a = 0; a < 5; a++) {
    let b = 20;
    console.log("a:", a, "b:", b);
}
console.log("Outside the loop -", "a:", a, "b:", b); // variables are not accessible


// const
for (let x = 0; x < 5; x++) {
    const y = 20;
    y = 10; // re-assignment not allowed
}

console.log(y); // constant is not accessible
