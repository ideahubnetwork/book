function factorial(num) {
    if (num <= 1) {
        return 1;
    } else{
        return num*arguments.callee(num-1);
    }
}

var factorial2 = (function f(num) {
    if (num <= 1)
        return 1;
    else
        return num * f(num-1);
})

var another = factorial;
factorial = null;
var t = another(5);
console.log(t);

t = factorial2(5);
console.log(factorial2(5));