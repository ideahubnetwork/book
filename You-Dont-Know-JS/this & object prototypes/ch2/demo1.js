// binding for primitive value
function log() {
  console.log(this);
}

log.call(3);


// demo2: binding for f.name
var bar = log.bind(this);
console.log(bar.name);    // bound log

// demo3: binding for arrow function
var a = 10;
var getA = () => console.log(this.a);
getA.call({ a: 3 });

