#!/usr/bin/node

let file = process.argv[2];

let fs = require('fs');

fs.readFile(file, function (err, data) {
  if (err) throw err;
  console.log(data.toString());
});
