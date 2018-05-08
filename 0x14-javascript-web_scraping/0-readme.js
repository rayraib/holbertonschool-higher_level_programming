#!/usr/bin/node

let file = process.argv[2];

let fs = require('fs');

fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
