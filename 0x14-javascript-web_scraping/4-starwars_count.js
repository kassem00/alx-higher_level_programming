#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;

    console.log(results.reduce(function (count, movie) {
      return movie.characters.find(function (character) {
        return character.endsWith('/18/');
      })
        ? count + 1
        : count;
    }, 0));
  }
});
