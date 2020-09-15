#!/usr/bin/node
const args = process.argv.slice(2);
if(args.length > 0)
{
    console.log(args[0]);
    return;
}
console.log('No argument');