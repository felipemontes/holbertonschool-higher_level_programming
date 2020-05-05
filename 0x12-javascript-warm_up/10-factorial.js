#!/usr/bin/node
const num = parseInt(process.argv[2]);

function Factorial (num) {
  if (isNaN(num)) {
    return (1);
  }
  if (num === 0) {
    return 1;
  } else {
    return num * Factorial(num - 1);
  }
}

console.log(Factorial(num));
