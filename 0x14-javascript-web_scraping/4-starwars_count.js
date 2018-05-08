#!/usr/bin/node

let url = process.argv[2];
let request = require('request');
let compare = 'https://swapi.co/api/people/18/';
let count = 0;

request(url, function (error, response, body) {
  if (error) throw error;
  let content = JSON.parse(body);
  let results = content['results'];
  //  console.log(results[1])
  for (let i = 0; i < results.length; i++) {
    let content = results[i];
    let characters = content['characters'];
    for (let i = 0; i < characters.length; i++) {
      if (characters[i] === compare) {
        count++;
      }
    }
  }
  console.log(count);
});
