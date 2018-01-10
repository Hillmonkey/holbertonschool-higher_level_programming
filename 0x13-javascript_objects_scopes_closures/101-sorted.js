#!/usr/bin/node
'use strict';
const dict = require('./101-data').dict;
let dict2 = {};
Object.keys(dict).forEach(function (key) {
  if (typeof (dict2[dict[key]]) === 'undefined') {
    dict2[dict[key]] = [];
  }
  dict2[dict[key]].push(key);
});
console.log(dict2);
