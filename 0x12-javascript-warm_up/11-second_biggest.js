#!/usr/bin/node

let arg = process.argv;
let len = arg.length;
let big;
let sBig;
let i;

if (len <= 3) {
  console.log('0');
} else {
  if (parseInt(arg[2]) < parseInt(arg[3])) {
    big = parseInt(arg[3]);
    sBig = parseInt(arg[2]);
  } else {
    sBig = parseInt(arg[3]);
    big = parseInt(arg[2]);
  }
  for (i = 2; i < len; i++) {
    if (parseInt(arg[i]) > big) {
      sBig = big;
      big = parseInt(arg[i]);
    } else if (parseInt(arg[i]) < big && sBig < parseInt(arg[i])) {
      sBig = parseInt(arg[i]);
    }
  }
  console.log(sBig);
}
