#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./100-starwars_characters.js <FILM ID>');
  process.exit(1);
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Failed with status code: ${response.statusCode}`);
    process.exit(1);
  }

  characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {

    let url = characters[i];

    request(url, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
      }
      if (response.statusCode !== 200) {
        console.error(`Failed with status code: ${response.statusCode}`);
        process.exit(1);
      }
      console.log(JSON.parse(body).name);
    }
    );
  }

});
