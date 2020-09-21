#!/usr/bin/node
//hola
let number = -1;
exports.logMe = function (item){
    number += 1;
    console.log(`${number}: ${item}`);
}