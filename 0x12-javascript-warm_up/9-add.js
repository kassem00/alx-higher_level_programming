#!/usr/bin/node
// Script that prints the addition of two integers
const arg = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

if (isNaN(arg) || isNaN(arg2)) {
  console.log(NaN);
} else {
  add(arg, arg2);
}
