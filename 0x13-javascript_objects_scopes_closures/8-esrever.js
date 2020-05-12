#!/usr/bin/node

exports.esrever = function (list) {
  const nlist = [];
  let b = 0;

  for (let i = list.length - 1; i >= 0; i--) {
    nlist[b] = list[i];
    b++;
  }

  return nlist;
};
