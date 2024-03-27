#!/usr/bin/node
// read file
const fs = require('fs').promises;

async function readFile () {
  const argument = process.argv[2];

  try {
    const content = await fs.readFile(argument, { encoding: 'utf8' });
    console.log(content);
  } catch (err) {
    console.error(err); // Directly print the error object
  }
}

readFile();
