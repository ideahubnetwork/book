class P {
  foo () {
    console.log('P.foo');
  }
}

class C extends P {
  foo () {
    super();
  }
}

var c1 = new C();
c1.foo();
