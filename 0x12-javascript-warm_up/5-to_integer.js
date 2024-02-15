#!/usr/bin/node
// Get the command-line argument
const argument = process.argv[2];
const num = Math.floor(Number(argument));

let message;

if (isNaN(num)) {
  message = 'Not a number';
} else {
  message = `My number: ${num}`;
}

console.log(message);
