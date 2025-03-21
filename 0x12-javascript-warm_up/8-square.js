#!/usr/bin/node
// script print squar size define by num u print 
let arg = Number(process.argv[2]);

if (isNaN(arg) || arg === undefined) {
  console.log("Missing size");
} else {
  for (let i = arg; i > 0; i--) {
    console.log('X'.repeat(arg));
  }
}