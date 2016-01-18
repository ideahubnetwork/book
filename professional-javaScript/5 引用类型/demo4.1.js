num = 1234567890;
pattern = /(\d{1,3})(?=\d{3})/g;

result = num.toString().replace(pattern, '$&,');
console.log(result);
