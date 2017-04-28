// binding for arrow function
var foo = (x) => console.log(this.x, x)
var bar = function (x) { console.log(this.x, x) }

foo.call({ x: 3 }, 3)
bar.call({ x: 3 }, 3)
