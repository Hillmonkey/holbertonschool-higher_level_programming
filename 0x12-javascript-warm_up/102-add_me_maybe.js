#!/usr/bin/node
'use strict';
exports.addMeMaybe = function (x, theFunction) {
  x++;
  theFunction(x);
};
