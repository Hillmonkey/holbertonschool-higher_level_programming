#!/usr/bin/node
'use strict';
let arraySize = process.argv.length - 2;
if (arraySize < 2) {
  console.log(0);
} else {
  let subArray = process.argv.slice(2, process.argv.length);
  subArray.sort().reverse();
  console.log(subArray);
  console.log(subArray[1]);
}
