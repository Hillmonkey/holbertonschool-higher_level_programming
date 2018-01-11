#!/usr/bin/node
'use strict';
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {}
  console.log(response.body);
  fs.writeFile(file, response.body, 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    }
  });
});
