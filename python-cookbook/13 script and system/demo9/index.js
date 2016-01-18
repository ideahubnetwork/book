var path = require('path');
var fs = require('fs');

var scandir = function(dir, callback) {
    fs.readdir(dir, function(err, files) {
        files.forEach(function(file) {
            file = path.join(dir, file);
            fs.stat(file, function(err, stats) {
                if (stats.isFile())
                    console.log(file);
            });
        });
    });
}

scandir('..')

