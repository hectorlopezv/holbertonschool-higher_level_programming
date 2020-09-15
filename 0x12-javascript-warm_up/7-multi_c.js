#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length > 0 && !Number.isNaN(parseInt(args[0])))
{
    const num = parseInt(args[0]);
    
    if (num < 0)
    {
        return;
    }
    for (let index = 0; index < num; index++) {
        console.log('C is fun')
    }
    return;
}

console.log('Missing number of occurrences');