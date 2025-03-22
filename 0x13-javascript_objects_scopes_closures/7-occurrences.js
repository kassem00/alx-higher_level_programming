#!/usr/bin/node
// Class Square that inherits from Square of 5-square.js
exports.nbOccurences = function (list, searchElement) {
  let last_found = list.indexOf(searchElement);
  let counter = 0;

  while (last_found != -1) {
    counter++;
    last_found = list.indexOf(searchElement, last_found + 1);
  }
  return counter;
}