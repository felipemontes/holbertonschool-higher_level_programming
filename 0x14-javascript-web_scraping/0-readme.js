#!/usr/bin/node

const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
