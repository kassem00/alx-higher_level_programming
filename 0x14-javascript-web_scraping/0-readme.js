#!/usr/bin/node
// read file
const fs = require('fs').promises;

async function readFile () {
  const argument = process.argv[2];

  try {
    const content = await fs.readFile(argument, { encoding: 'utf8' });
    console.log(content);
  } catch (err) {
    if (err.code === 'ENOENT') {
      console.error(`Error: The file "${argument}" does not exist.`);
    } else {
      console.error('Error reading file:', err);
    }
  }
}

readFile();
