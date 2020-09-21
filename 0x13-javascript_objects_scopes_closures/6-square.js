#!/usr/bin/node
//hola
const sq = require('./5-square');

class Square extends sq{
    
    charPrint(c){
        if (typeof c !== 'undefined')
        {
            for (let i = 0; i < this.size; i++) {
                console.log(c.repeat(this.size))
            }
            return;
        }
        for (let i = 0; i < this.size; i++) {
            console.log('X'.repeat(this.size))
        }
    }
}

module.exports = Square;
