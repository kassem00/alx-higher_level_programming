#!/usr/bin/node
// Class Square that inherits from Square of 5-square.js
const BaseSquare = require('./5-square.js');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
