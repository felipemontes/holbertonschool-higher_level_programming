#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], function (error, response, body) {
  if (error == null) {
    const ids = [];
    const res = JSON.parse(body);
    var count = {};
    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        ids.push(res[i].userId);
      }
    }
    ids.forEach(function (i) { count[i] = (count[i] || 0) + 1; });
    console.log(count);
  }
});
