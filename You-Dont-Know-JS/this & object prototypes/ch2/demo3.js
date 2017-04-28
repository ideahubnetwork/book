// Indirection Reference

function foo () {
  console.log(this.a);
}

var a = 2;
global.a = 2;         // for node environment

var o = { a: 3, foo: foo }
var p = { a: 4 }

foo();                  // 2
o.foo();                // 3 
(o.foo)();              // 3
(p.foo = o.foo)();      // 2
