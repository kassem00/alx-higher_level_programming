#!/usr/bin/node
// script that computes and prints a factorial
const arg1 = Number(process.argv[2]);

function fact (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

if (isNaN(arg1) || arg1 === undefined) {
  console.log('1');
} else {
  console.log(`${fact(arg1)}`);
}
