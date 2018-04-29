#!/usr/bin/node

let arg = process.argv;
let value, i, cValue;

if (arg.length <= 2 || typeof (arg[2] === 'string')) {
  console.log('Missing size');
} else {
  value = parseInt(arg[2]);
  cValue = value;
  while (value > 0) {
    let string = '';
    for (i = cValue; i > 0; i--) {
      string += 'X';
    }
    console.log(string);
    value--;
  }
}
