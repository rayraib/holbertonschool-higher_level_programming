#!/usr/bin/node

// import the Rectangle class from 4-rectangle module
const Rectangle = require('./4-rectangle');

// define square that extends from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // call the constructor method of Rectangle with size as both args
    super(size, size);
  }
}

module.exports = Square;
