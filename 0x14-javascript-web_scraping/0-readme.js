#!/usr/bin/node
//hola
const args = process.argv.slice(2);
const fs = require('fs');

fs.readFile(args[0], 'utf-8', (error, data) => {
    console.log(error || data);
});
