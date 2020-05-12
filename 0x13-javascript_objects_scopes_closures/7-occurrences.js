#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  var cont = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      cont += 1;
    }
  }
  return cont;
};
