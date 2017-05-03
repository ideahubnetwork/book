function Bar () {
  this.a = 3;
  this.b = 4;
}

Bar.prototype.hello = function () {
  console.log('hello, bar');
}

var bar = new Bar();
console.log(bar);




function Foo () {
  Bar.call(this);
}

Foo.prototype = new Bar();

Foo.prototype.say = function () {
  console.log('hello, foo');
}

Foo.prototype.constructor = Foo;

var foo = new Foo();
console.log(foo);




function Baz () {
  Bar.call(this);
}

Baz.prototype = Object.create(Bar.prototype);

Baz.prototype.say = function () {
  console.log('hello, baz');
}

Baz.prototype.constructor = Baz;
