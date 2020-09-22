#!/usr/bin/node
//hola
const args = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(args[0], args[1], error => {
    if(error){
        console.log(error);
    }
});