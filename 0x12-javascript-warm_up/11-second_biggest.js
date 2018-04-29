#!/usr/bin/node

let arg = process.argv;
let len = arg.length;
let big;
let sBig;
let i;

if (len <= 3) {
  console.log('0');
} else {
  if (arg[2] < arg[3]) {
    big = arg[3];
    sBig = arg[2];
  } else {
    sBig = arg[3];
    big = arg[2];
  }
  for (i = 2; i < len; i++) {
    if (parseInt(arg[i]) > big) {
      sBig = big;
      big = parseInt(arg[i]);
    } else if (sBig < parseInt(arg[i])) {
      sBig = parseInt(arg[i]);
    }
  }
  console.log(sBig);
}
