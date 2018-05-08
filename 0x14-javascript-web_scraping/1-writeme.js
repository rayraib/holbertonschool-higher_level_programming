#!/usr/bin/node

let file = process.argv[2];
let content = process.argv[3];

let fs = require('fs');

fs.writeFile(file, content, 'utf-8', function (err) {
  if (err) throw err;
});
