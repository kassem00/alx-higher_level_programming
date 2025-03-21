const Square = require('./4-rectangle.js');


module.exports = class Rectangle extends Square {
  constructor(size) {
    super();
    this.size = size;
  }
}