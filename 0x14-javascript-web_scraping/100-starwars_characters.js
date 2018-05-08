#!/usr/bin/node

const request = require('request');
let id = process.argv[2];

let url = 'https://swapi.co/api/films/' + id;

request(url, function (error, response, body) {
  if (error) throw error;
  let content = JSON.parse(body);

  let characters = content['characters'];
  for (let i = 0; i < characters.length; i++) {
    let personUrl = characters[i].replace(/["]+/g, '');
    request(personUrl, function (error, response, body) {
      if (error) throw error;
      let personContent = JSON.parse(body);
      let name = personContent['name'];
      console.log(name);
    });
  }
});
