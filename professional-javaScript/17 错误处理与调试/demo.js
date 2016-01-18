"use strict"
class HttpError extends Error {
  constructor(message) {
    this.name = 'HttpError';
    this.message = message;
  }

}

function CustomError(message) {
    this.name = 'CustomError';
    this.message = message;
}

CustomError.prototype = new Error();

var test = function(a) {
    if (a == -1)
        throw new HttpError('this is a ');
}

try {
    test(-1)
} catch(err) {
    console.log(err.message);
}

