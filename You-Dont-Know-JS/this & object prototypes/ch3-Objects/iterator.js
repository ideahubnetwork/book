var l = [1, 2, 3, 4, 5];

for (var i of l) {
  console.log(i);
}



var o = {
  a: 3,
  b: 4,
  c: 5
};

try {
  for (var i of o) {
    console.log(i);
  }
} catch (e) {
  console.error(e.message); // o[Symbol.iterator] is not a function
}

var randoms = {
  [Symbol.iterator]: function () {
    return {
      next () {
        return { value: Math.random() } 
      }
    } 
  }
}

for (var i of randoms) {
  console.log(i);
}
