#!/usr/bin/node
let array = [];
let b = 0;

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    array[b] = parseInt(process.argv[i]);
    b++;
  }
  array = array.sort();
  array = array.reverse();
  console.log(array[1]);
}
