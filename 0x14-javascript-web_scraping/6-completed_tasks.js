#!/usr/bin/node

const request = require('request');

let url = process.argv[2];
let result = {};

request(url, function (error, response, body) {
  if (error) throw error;
  let content = JSON.parse(body);

  for (let i = 0; i < content.length; i++) {
    let task = content[i];

    let key = task['userId'];
    let stat = task['completed'];
    if (stat === true) {
      if (key in result) {
        result[key]++;
      } else {
        result[key] = 1;
      }
    }
  }
  console.log(result);
});
