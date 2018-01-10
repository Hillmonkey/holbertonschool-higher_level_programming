#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof (counter) === 'undefined') {
    counter = 0;
  }
  console.log(counter + ': ' + item);
  counter++;
};
