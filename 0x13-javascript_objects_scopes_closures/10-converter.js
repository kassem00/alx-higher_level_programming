#!/usr/bin/node
// Function that returns a converter for a given base
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
