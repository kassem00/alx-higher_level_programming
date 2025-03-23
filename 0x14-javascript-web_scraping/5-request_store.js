#!/usr/bin/node
// Script that fetches a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
} else {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error('Error:', error.message);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to fetch URL. Status code: ${response.statusCode}`);
    } else {
      fs.writeFile(process.argv[3], body, { encoding: 'utf8' }, (err) => {
        if (err) {
          console.error('Error writing to file:', err.message);
        }
      });
    }
  });
}
