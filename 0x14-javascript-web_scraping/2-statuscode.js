#!/usr/bin/node

let request = require('request');

let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;
  console.log('code: ' + response.statusCode);
});
