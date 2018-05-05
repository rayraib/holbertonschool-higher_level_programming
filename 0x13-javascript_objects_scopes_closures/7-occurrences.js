#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  if (!list.includes(searchElement)) {
    return (0);
  } else {
    let count = 0;
    let len = list.length - 1;

    while (len >= 0) {
      if (list[len] === searchElement) {
        count++;
      }
      len--;
    }
    return (count);
  }
};
