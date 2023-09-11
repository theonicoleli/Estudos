function multiply(multiplier, ...theArgs) {
    return theArgs.map((x) => multiplier * x);
}

const arr = multiply(2,1,2,3);
console.log(arr)