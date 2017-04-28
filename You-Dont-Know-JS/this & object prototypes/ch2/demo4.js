// hard binding

function foo () {
  console.log(this.a);
}


var bar = foo.bind({ a:3 }).bind({ a:4 });
bar();
