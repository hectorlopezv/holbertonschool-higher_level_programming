#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length > 0)
{
    const num = parseInt(args[0]);
    
    if (Number.isNaN(num))
    {
        console.log('Not a number');
        return;
    }
    console.log(`My number: ${num}`);
    return;
}

console.log('Not a number');