#!/usr/bin/node
const args = process.argv.slice(2);

function add(a, b)
{
    return parseInt(a) + parseInt(b);
}
const resu = add(args[0], args[1]);
console.log(resu);