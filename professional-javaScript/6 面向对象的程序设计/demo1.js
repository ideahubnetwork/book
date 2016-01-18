// demo1 工厂模式
function createPerson(name, age, job) {
    var obj = new Object();
    obj.name = name;
    obj.age = age;
    obj.job = job;
    obj.sayName = function() {
        console.log(this.name);
    }
    return obj;
}

var person1 = createPerson('tiantian', 20, 'student');

// Question: 如何知道这个对象的类型？

// demo2 构造函数模式
function Person(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;
    this.sayName = function() {
        console.log(this.name);
    }
    this.sayName2 = new Function('console.log(this.name)');
}

var tian = new Person('tiantian', 20, 'student');
var jing = new Person('jingjing', 20, 'student');
console.log(`demo2: ${tian.sayName === jing.sayName}`);

// Question: 方法每次都被实例化，导致不同的作用域链和标识符解析。

// demo3 原型模式
function Person2() {
    this.neme = 'tian'
}
Person2.prototype.name = 'tiantian';
Person2.prototype.age = 20;
Person2.prototype.job = 'student';
Person2.prototype.sayName = function() {
    console.log(this.name);
}

var tian = new Person2() 
console.log(tian);


