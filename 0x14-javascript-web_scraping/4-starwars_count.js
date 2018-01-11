#!/usr/bin/node
'use strict';
const request = require('request');
const url = process.argv[2];
const wedgeAntilles = 'https://swapi.co/api/people/18/';
request(url, function (error, response, body) {
  if (error) {}
  let count = JSON.parse(response.body).count;
  let starWarsJSON = JSON.parse(response.body).results;
  let movieCount = 0;
  for (let i = 0; i < count; i++) {
    // console.log(starWarsJSON[i].title);
    let characters = starWarsJSON[i].characters;
    for (let character of characters) {
      // console.log(character, typeof(character));
      if (character === wedgeAntilles) {
        movieCount++;
      }
    }
  }
  console.log(movieCount);
});
