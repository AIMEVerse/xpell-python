
let startIndex = 0;



class NameCheckerClass {

    static #instance = null;

    static getInstance() {
        if (this.#instance === null) {
            this.#instance = new NameCheckerClass();
        }
        return this.#instance;
    }


    #engine = "google";

    check(name) {
        if (name.length < 4) {
            console.log("Name is too short " + name);
            return false;
        }
        return true;
    }

    get engine() {
        return this.#engine;
    }

    set engine(value) {
        if(value === "google" || value === "yandex")
        this.#engine = value;
    }
}

// const NameChecker = new NameCheckerClass();


class User {
    constructor(name) {
        this.id = startIndex++;
        this.name = name;
    }

    checkName() {
        // console.log(NameCheckerClass.hasOwnProperty("engine"));
        const nc  = NameCheckerClass.getInstance();
        if(nc.engine === "google")
            return nc.check(this.name)
    
    }

    sayHi() {
        alert(this.id + ":" + this.name);
    }
}




const user = new User("Joh"); //id 0
const user2 = new User("Pete"); //id 1

user.checkName();
user2.checkName();