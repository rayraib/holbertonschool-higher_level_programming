#!/usr/bin/node

exports.esrever = function (list) {
  let max = list.length;
  let newList = new Array(max);
  let j = max - 1;
  for (let i = 0; i < max; i++) {
    newList[j] = list[i]; j--;
  }
  return (newList);
};
