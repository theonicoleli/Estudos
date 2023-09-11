const car = {make: 'Toyota', model: 'Camry'};

console.log(Object.keys(car));
console.log(Object.values(car));
console.log(Object.entries(car));

const details = {color: 'red'};
const carWithDetails = Object.assign({}, car, details);

console.log(carWithDetails);

//Object.freeze(car);

car.year = 2023;

console.log(car.year);

console.log(Object.is('hello', 'hello'));
console.log(Object.is(NaN, NaN));

Object.defineProperty(car, 'year', {value: 2020, writable: false});
console.log(car.year);

Object.defineProperty(car, 'year', {value: 2020, writable: true});
console.log(car.year);

console.log(car.hasOwnProperty('make'));
console.log(car.hasOwnProperty('ratatouile'));