#!/usr/bin/node
<<<<<<< HEAD
// script that prints a message depending
// of the number of arguments passed
||||||| 4ca8b7a
//script that prints a message depending of the number of arguments passed
=======
// script that prints a message depending of the number of arguments passed
>>>>>>> refs/remotes/origin/master
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
