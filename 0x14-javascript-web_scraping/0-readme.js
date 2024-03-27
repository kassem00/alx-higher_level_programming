#!/usr/bin/node
// read from file

const fs = require('fs').promises;
const filename = process.argv[2];


async function readFile() {
  try {
    const data = await fs.readFile(filename, { encoding: 'utf8' });
    console.log(data); // Log the file content
  } catch (err) {
    if (err.code === 'ENOENT') {
      console.error(`Error: The file "${filename}" does not exist.`);
    } else {
      console.error('Error reading file:', err);
    }
  }
}

readFile();
