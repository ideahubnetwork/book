var o1 = {
  a: 3
};

Object.defineProperty(o1, 'b', {
  writable: false,
  enumerable: true,
  value: 4
})

Object.defineProperty(o1, 'c', {
  get () {
    return this._a; 
  },

  set (v) {
    this._a = v;
  },

  enumerable: true
})

o1.c = 5;

var o2 = Object.create(o1);
o2.a = 'a';
o2.b = 'b';
o2.c = 'c';

console.log(o1, o2);
console.log(o1.a, o1.b, o1.c);
console.log(o2.a, o2.b, o2.c);
