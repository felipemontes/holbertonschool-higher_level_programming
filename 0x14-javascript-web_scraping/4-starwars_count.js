#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    const res = json.results;
    let count = 0;
    for (let i = 0; i < res.length; i++) {
      const chars = res[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
