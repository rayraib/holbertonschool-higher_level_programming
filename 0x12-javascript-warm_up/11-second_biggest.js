#!/usr/bin/node

let arg = process.argv;
let len = arg.length;
let big = 0;
let pBig, i;

if (len <= 3) {
  console.log('0');
} else {
  for (i = 2; i < len; i++) {
    if (big < arg[i]) {
      pBig = big;
      big = arg[i];
    }
  }
  console.log(pBig);
}
