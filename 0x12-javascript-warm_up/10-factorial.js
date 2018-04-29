#!/usr/bin/node

let arg = process.argv;
let n = parseInt(arg[2]);

function fact (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  } else {
    return (a * fact(a - 1));
  }
}
let result = fact (n);
console.log(result);
