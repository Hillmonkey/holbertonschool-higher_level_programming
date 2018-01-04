#!/usr/bin/node
'use strict';
let size = Math.floor(process.argv[2]);
if ((typeof (process.argv[2]) === 'undefined') ||
    (isNaN(size))) {
  console.log('Missing size');
} else {
  let line = '';
  for (let s = 0; s < size; s++) {
    line += 'X';
  }
  for (let s = 0; s < size; s++) {
    console.log(line);
  }
}
