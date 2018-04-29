#!/usr/bin/node

let arg = process.argv;
let value;

if (arg.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  value = parseInt(arg[2]);
  while (value > 0) {
    console.log('C is fun');
    value--;
  }
}
