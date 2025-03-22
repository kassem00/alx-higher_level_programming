#!/usr/bin/node
// Function that reverses a list without using reverse()

exports.logMe = (function () {
  let count = 0;
  return function (item) {
    console.log(`${count}: ${item}`);
    count++;
  };
})();
