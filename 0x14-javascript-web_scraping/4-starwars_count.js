#!/usr/bin/node
// invoke this script as follows:
// ./4-starwars_count.js http://swapi.co/api/films

'use strict';
const request = require('request');
const url = process.argv[2];
const wedgeAntilles = '/18/';
request(url, function (error, response, body) {
  if (error) {}
  let count = JSON.parse(response.body).count;
  let starWarsJSON = JSON.parse(response.body).results;
  let movieCount = 0;
  for (let i = 0; i < count; i++) {
    let characters = starWarsJSON[i].characters;
    for (let character of characters) {
      if (character.endsWith(wedgeAntilles)) {
        movieCount++;
      }
    }
  }
  console.log(movieCount);
});
