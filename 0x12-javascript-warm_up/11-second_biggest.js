#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length > 1)
{
    const largo = args.length;
    const sortedArray = args.sort( (a,b)=> a-b);
    console.log(sortedArray[largo - 2]);
    return;
}
console.log('0');