#!/usr/bin/node
'use strict';
const fs = require('fs');

const fname = process.argv[2];
let data = fs.readFileSync(fname, 'utf8');
  console.log(data);
