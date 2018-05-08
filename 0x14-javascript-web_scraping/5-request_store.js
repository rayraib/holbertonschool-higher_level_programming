#!/usr/bin/node

const request = require('request');
const fs = require('fs');
let url = process.argv[2];
let file = process.argv[3];

request.open('GET', url);
request.response = 'text';
request.send();
