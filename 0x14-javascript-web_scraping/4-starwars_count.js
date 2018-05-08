#!/usr/bin/node

let url = 'http://swapi.co/api/people/18';
let request = require('request');

request(url, function (error, response, body) {
  if (error) throw error;
  let content = JSON.parse(body);
  let movies = content['films'].length;
  console.log(movies);
});
