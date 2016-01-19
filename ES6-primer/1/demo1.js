'use strict';


// demo1
// 在ES6中，函数本身的作用域在块级作用域内，在ES5中没有块级作用域，所以在
// ES6中，函数f会触犯ReferenceError。
{
    function f() {
        console.log('inside');
    }
}
// f();    // ReferenceError


// demo2
var a = 3;
let b = 4;
console.log(global.a);      // undefined
console.log(global.b);      // undefined

global.a = 3;
console.log(global.a);      // 3