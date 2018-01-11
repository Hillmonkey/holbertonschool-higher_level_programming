#!/usr/bin/node
'use strict';
const request = require('request');
const request2 = require('request');
const episodeID = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeID;

request(url, function (error, response, body) {
  if (error) {}
  let movieCharacters = JSON.parse(response.body).characters;
  console.log(movieCharacters);
  for (let character in movieCharacters) {
    console.log("=========================");
    console.log(movieCharacters[character]);
    let charUrl = movieCharacters[character];
    // console.log(char);
    request2(charUrl, function (error2, response2, body2) {
      if (error2) {}
      // console.log(JSON.parse(response2));
      let aCharacter = JSON.parse(response2.body2);
      console.log(aCharacter);
    });
    console.log("+++++++++++++++++++++");
    // break;
  }
});
