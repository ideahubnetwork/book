# 错误处理

## try-catch语句
``` javascript
try {

} catch(err) {
    console.log(err.message);
}
```

1. finally
finally语句总会执行，无论try，catch语句中包含什么代码，甚至return。

2. 错误类型
+ Error
+ EvalError
+ RangeError
+ ReferenceError
+ SyntaxError
+ TypeError
+ URIError

``` javascript
try {

} catch (err) {
    if (err instanceof TypeError) {

    } else if (err instanceof ReferenceError) {

    } else {

    }
}
```

3. 抛出错误
利用原型链可以通过继承Error来创建自定义错误类型。

``` js

```