#!/usr/bin/node

let file = process.argv[2];

let fs = require('fs');

fs.readFile(file, 'utf-8', function (err, data) {
  if (err) throw err;
  process.stdout.write(data);
});
