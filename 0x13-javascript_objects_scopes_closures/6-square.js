#!/usr/bin/node
'use strict';
// const Rectangle = require('./4-rectangle');
const Square5 = require('./5-square');
const Square = class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    let line = '';
    // console.log("this.size " + this.size + "<<<");
    // console.log("this.height " + this.height + "+++");
    for (let i = 0; i < this.height; i++) {
      line += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
};
module.exports = Square;
