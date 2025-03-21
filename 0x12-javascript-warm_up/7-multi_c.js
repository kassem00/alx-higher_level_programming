#!/usr/bin/node
// script print number of c is fun u have to pass number
let arg = Number(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  if (arg > 0) {
    while (arg) {
      console.log('C is fun');
      arg--;
    }
  }
}
