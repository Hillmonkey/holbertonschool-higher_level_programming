#!/usr/bin/node
'use strict';

exports.esrever = function (list) {
  var ret = [];
  for (var i = list.length - 1; i >= 0; i--) {
    ret.push(list[i]);
  }
  return ret;
};
