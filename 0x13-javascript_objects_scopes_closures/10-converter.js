#!/usr/bin/node

exports.converter = function (base) {
  function some (x) {
    if (base === 10) {
      return (parseInt(x, base));
    } else {
      return (x.toString(base));
    }
  }
  return (some);
};
