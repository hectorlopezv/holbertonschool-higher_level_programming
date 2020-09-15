#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length > 0 && !Number.isNaN(parseInt(args[0])))
{
    const num = parseInt(args[0]);
    const str_ = 'X';
    if (num < 0)
    {
        return;
    }
    for (let index = 0; index < num; index++) {
        console.log(str_.repeat(num));
    }
    return;
}

console.log('Missing size');