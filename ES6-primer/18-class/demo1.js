'use strict'
class Point {
  constructor (x, y) {
    this.x = x
    this.y = y
  }

  sum () {
    return this.x + this.y
  }
}

class SuperPoint extends Point {
  constructor (x, y) {
    // console.log('before', this)
    super(x, y)
    console.log('after', this)
  }

  mul () {
    console.log('mul', this)
    return this.x * this.y
  }
}

const s = new SuperPoint(3, 4)

console.log(s.x, s.y, s.sum(), s.mul())