#!/usr/bin/node
// prints the second max

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.sort();
  console.log(array.reverse()[1]);
}
