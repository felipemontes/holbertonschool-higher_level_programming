#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    this.chr = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(`${this.chr.repeat(this.width)}`);
    }
  }
}

module.exports = Rectangle;
