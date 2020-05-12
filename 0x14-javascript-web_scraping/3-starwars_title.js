#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/id'.replace('id', process.argv[2]);

request(url, function (error, response, body) {
  if (error == null) {
    const res = JSON.parse(body);
    console.log(res.title);
  }
});
