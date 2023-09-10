class Pet {
    constructor(animal, age, weight) {
        this.animal = animal;
        this.age = age;
        this.weight = weight;
    }

    get _animal() {return this.animal};
    get _age() {return this.age};
    get _weight() {return this.weight};

    set _typeAnimal(animal) {this.animal = animal};
    set _typeAge(age) {this.age = age};
    set _typeWeight(weight) {this.weight = weight};
}

class Dog extends Pet{
    constructor(animal, age, weight, name) {
        super(animal, age, weight);
        this.name = name;
    }

    get _name() {return this.name};

    set _typeName(name) {this.name = name};

    dogPerfil() {
        let textDog = "Animal: " + this.animal + ", Age: " + this.age + ", Weight: " + this.weight + ", Name: " + this.name;
        console.log(textDog);
    }
}


const dogOne = new Dog("Dog", 12, 9, "Roberto");

console.log(dogOne._animal);
console.log(dogOne._age);
console.log(dogOne._weight);
console.log(dogOne._name);
dogOne.dogPerfil();

dogOne._typeName = "Ricardo";

dogOne.dogPerfil();