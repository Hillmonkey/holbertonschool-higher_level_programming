#!/usr/bin/node
'use strict';
const Rectangle = require('./4-rectangle');
const Square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = Square;
