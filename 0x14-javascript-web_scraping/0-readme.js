#!/usr/bin/node
'use strict';
const fs = require('fs');
const fname = process.argv[2];

// this gives me a buffer object without utf8 specified ...
fs.readFile(fname, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
