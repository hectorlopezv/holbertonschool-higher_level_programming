#!/usr/bin/node
//una clase basicamente.... como en programacion functional
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};