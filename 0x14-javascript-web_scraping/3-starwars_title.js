#!/usr/bin/node
const request = require('request');
let eps = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(eps, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
    data = JSON.parse(body);
    console.log(data.title);
});
