#!/usr/bin/node
'use strict';
const fs = require('fs');
const fname = process.argv[2];
const text = process.argv[3];

fs.writeFile(fname, text, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
