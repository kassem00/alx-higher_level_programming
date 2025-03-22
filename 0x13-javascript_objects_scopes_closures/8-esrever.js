#!/usr/bin/node
// Function that reverses a list without using reverse()
exports.esrever = function (list) {
  const reversed = [];
  for (let i = 0; i < list.length; i++) {
    reversed[list.length - 1 - i] = list[i];
  }
  return reversed;
};
