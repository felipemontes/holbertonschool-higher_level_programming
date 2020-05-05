#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
const hash = 'X';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log(`${hash.repeat(num)}`);
  }
}
