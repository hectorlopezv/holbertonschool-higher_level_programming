#!/usr/bin/node
//hola
exports.esrever = function (list){

    let arr = [];
    while(list.length > 0){
        arr.push(list.pop());
    }
    return arr;
}