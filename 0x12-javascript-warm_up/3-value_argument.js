#!/usr/bin/node

let arg = process.argv;
let value = (arg[2]);

if (String('undefined').valueOf() === String(value).valueOf()) {
  console.log('No argument');
} else {
  console.log(value);
}
