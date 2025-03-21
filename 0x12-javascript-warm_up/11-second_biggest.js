#!/usr/bin/node
// Script that finds the second biggest integer in the list of arguments
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => a - b);
  console.log(sortedArgs[sortedArgs.length - 2]);
}
