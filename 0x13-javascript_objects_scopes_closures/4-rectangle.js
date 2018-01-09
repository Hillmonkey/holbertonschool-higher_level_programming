#!/usr/bin/node
'use strict';
const Rectangle = class Rectangle {
  constructor (width, height) {
    if ((width > 0) && (height > 0)) {
      this.width = width;
      this.height = height;
    }
  }
  print () {
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
module.exports = Rectangle;
