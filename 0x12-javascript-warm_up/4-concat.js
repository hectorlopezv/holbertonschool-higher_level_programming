#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length > 1)
{
    console.log(`${args[0]} is ${args[1]}`);
    return;
}
else if (args.length === 1)
{
    console.log(`${args[0]} is undefined`);
}
else
{
    console.log('undefined is undefined');
}