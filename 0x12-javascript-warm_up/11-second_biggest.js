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
  pBig = parseInt(arg[3]);
  for (i = 2; i < len; i++) {
    if (big < arg[i]) {
      pBig = big;
      big = arg[i];
    }
  }
  if (big > pBig) {
    console.log(pBig);
  } else {
    console.log(big);
  }
}
