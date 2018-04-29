#!/usr/bin/node

let arg = process.argv;
let len = arg.length;
let big;
let pBig;
let i;

if (len <= 3) {
  console.log('0');
} else {
  big = parseInt(arg[2]);
  pBig = big;
  for (i = 2; i < len; i++) {
    if (big < parseInt(arg[i])) {
      pBig = big;
      big = parseInt(arg[i]);
    }
  }
  console.log(pBig);
}
