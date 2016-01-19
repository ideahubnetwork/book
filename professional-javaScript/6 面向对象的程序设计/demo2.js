var xian = {
    index: 0
}

Object.defineProperty(xian, 'top', {
    configurable: true,
    get: function() {
        return this.index * 100;
    }
});

console.log(xian.top);
xian.index = 20;
console.log(xian.top);