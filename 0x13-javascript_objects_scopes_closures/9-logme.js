#!/usr/bin/node
/* logMe: prints the number of argument already printed
 * and the new argument value
 */
let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
