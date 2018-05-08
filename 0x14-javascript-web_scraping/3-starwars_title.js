#!/usr/bin/node

let epNum = process.argv[2];
let request = require('request');
let url = 'http://swapi.co/api/films/' + epNum;

request(url, function (error, response, body) {
  if (error) throw error;
  let content = JSON.parse(body);// parse the string content to an object
  let title = content['title'];
  console.log(title);
});
