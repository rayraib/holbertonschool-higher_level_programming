#!/usr/bin/node

let arg = process.argv;
let value;

if (arg.length <= 2) {
  console.log('Not a number');
} else if (typeof (arg[2]) === 'string') {
  value = parseInt(arg[2]);
  if (isNaN(value)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + value);
  }
} else if (typeof (arg[2]) === 'undefined') {
  value = Math.floor(arg[2]);
  if (isNaN(value)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + value);
  }
}
