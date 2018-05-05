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
      console.log('X'.repeat(x));
      cpHeight--;
    }
  }

  // instance method: swap height and width values
  rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // instance method: double the width and height value
  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
