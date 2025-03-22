#!/usr/bin/node
// Class Square that inherits from Square of 5-square.js
exports.nbOccurences = function (list, searchElement) {
  let LastFound = list.indexOf(searchElement);
  let counter = 0;

  while (LastFound !== -1) {
    counter++;
    LastFound = list.indexOf(searchElement, LastFound + 1);
  }
  return counter;
};
