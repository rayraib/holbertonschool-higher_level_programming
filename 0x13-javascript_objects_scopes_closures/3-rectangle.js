#!/usr/bin/node

class Rectangle {
  // constructor for class Rectangle: assings height and width
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // instance method
  print () {
    let cpHeight = this.height;
    while (cpHeight > 0) {
      let x = this.width;
      console.log('x'.repeat(x));
      cpHeight--;
    }
  }
}
module.exports = Rectangle;
