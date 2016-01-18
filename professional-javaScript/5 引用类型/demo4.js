var text = 'this has been a short ahort bhort sumer'
var pattern = /(.)(?=hort)/g

if (pattern.exec(text)) {
    console.log(RegExp['$&']);

    console.log(RegExp.$1);

    console.log(text.match(pattern));
}

result = text.replace(pattern, '($1)')
console.log(result);
