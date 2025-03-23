#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./101-starwars_characters.js <FILM ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(new Error(`Error: ${error.message}`)); // Reject with an Error object
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed with status code: ${response.statusCode}`)); // Reject with an Error object
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function printCharacters () {
  try {
    const movieData = await fetchData(url);
    const charactersUrls = movieData.characters;

    for (const characterUrl of charactersUrls) {
      const characterData = await fetchData(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error.message); // Log the error message
    process.exit(1);
  }
}

printCharacters();
