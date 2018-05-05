#!/usr/bin/node

// import the Rectangle class from 4-rectangle module
const S = require('./5-square');

// define square that extends from Rectangle
class Square extends S {
  constructor (size) {
    // call the constructor method of Rectangle with size as both args
    super(size, size);
  }
  // instance method: prints the rectangle using the character c
  charPrint (c) {
    // if c is not defined invoke the super method print()
    if (c === undefined) {
      super.print();
    } else {
      let x = this.width;
      let y = x;
      while (y > 0) {
        console.log(c.repeat(x));
        y--;
      }
    }
  }
}

module.exports = Square;
