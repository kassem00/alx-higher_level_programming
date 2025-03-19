#!/usr/bin/node
// script print number of c is fun u have to pass number
let arg = Number(process.argv[2]);

if (arg == NaN) {
  console.log("Missing number of occurrences");
} else {

  while (arg) {
    console.log("C is fun");
    arg--;
  }
}