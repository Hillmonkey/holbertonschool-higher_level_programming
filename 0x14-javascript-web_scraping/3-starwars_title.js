#!/usr/bin/node
'use strict';
const request = require('request');
const episodeID = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeID;

request(url, function (error, response, body) {
  if (error) {}
  let starWarsJSON = JSON.parse(response.body);
  console.log(starWarsJSON.title);
});
