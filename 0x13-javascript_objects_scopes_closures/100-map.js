#!/usr/bin/node

const l = require('./100-data').list;
console.log(l);
const map1 = l.map(x => x * (x - 1));
console.log(map1);
