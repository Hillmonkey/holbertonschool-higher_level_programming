#!/usr/bin/node
'use strict';
exports.nbOccurences = function (list, el) {
  let count = 0;
  for (let s of list) {
    if (s === el) {
      count++;
    }
  }
  return (count);
};
