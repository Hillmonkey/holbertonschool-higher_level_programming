#!/usr/bin/node
'use strict';
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {}
  console.log('code:', response && response.statusCode);
});
