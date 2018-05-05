#!/usr/bin/node

const l = require('./100-data').list;
console.log(l);
const map1 = l.map(x => x * l.indexOf(x));
console.log(map1);
