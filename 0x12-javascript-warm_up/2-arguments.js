#!/usr/bin/node
const args = process.argv.slice(2);
if(args.length > 0)
{
    console.log('Argument found');
    return;
}
console.log('No argument');
