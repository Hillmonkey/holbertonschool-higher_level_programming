#!/usr/bin/node

exports.converter = function (base) {
  function convertBase (number) {
    // return (parseInt(number, base));
    return number.toString(base);
  }
  return convertBase;
};
