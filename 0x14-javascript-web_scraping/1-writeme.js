#!/usr/bin/node

const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
