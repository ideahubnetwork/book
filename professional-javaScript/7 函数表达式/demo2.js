function compare(prop) {
    return function(obj1, obj2) {
        var value1 = obj1[prop];
        var value2 = obj2[prop];
        if (value1 < value2) {
            return -1;
        } else if(value1 > value2){
            return 1;
        } else {
            return 0;
        }
    }
}

var obj1 = {
    a: 1
};

var obj2 = {
    a: 4
};

var flag = compare('a')(obj1, obj2);
console.log(flag);