#!/usr/bin/node
'use strict';
if ((typeof (process.argv[2]) === 'undefined') ||
    (isNaN(Math.floor(process.argv[2])))) {
  console.log('Missing number of occurrences');
} else {
  for (let s = 0; s < Math.floor(process.argv[2]); s++) {
    console.log('C is fun');
  }
}
