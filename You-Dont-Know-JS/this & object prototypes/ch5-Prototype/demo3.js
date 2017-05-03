function Foo () {

}

var foo = new Foo();

var r1 = foo instanceof Foo;
var r2 = foo.__proto__ === Foo.prototype;
var r3 = Foo.prototype.isPrototypeOf(foo);

console.log(r1, r2, r3);


var a = {};
var b = Object.create(a);

var r4 = a.isPrototypeOf(b);

console.log(r4);
