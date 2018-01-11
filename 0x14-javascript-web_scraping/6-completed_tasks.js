#!/usr/bin/node
'use strict';
const request = require('request');
const url = process.argv[2];
// run script by passing this as a command line arg:
// https://jsonplaceholder.typicode.com/todos

request(url, function (error, response, body) {
  if (error) {}
  let todoJSON = JSON.parse(response.body);
  let todoDict = {};
  // console.log(todoJSON);
  for (let el of todoJSON) {
    if (el.completed) {
      if (typeof (todoDict[el.userId]) === 'undefined') {
        todoDict[el.userId] = 0;
      }
      todoDict[el.userId]++;
    }
  }
  console.log(todoDict);
});
