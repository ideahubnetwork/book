var o = {
  get a () {
    return 10; 
  }
}

Object.defineProperty(o, 'b', {
  get () {
    return this.a * 2; 
  },
  enumerable: true
})

console.log(o.a, o.b);
o.a = 20;
console.log(o.a, o.b);
