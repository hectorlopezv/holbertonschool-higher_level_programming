#!/usr/bin/node
//hola
class Rectangle {
    constructor(w, h){
        if (parseInt(w) > 0 && parseInt(h) > 0)
        {
            this.width = w;
            this.height = h;
        }
    }
    
    print()
    {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width))
        }
    }
    rotate(){
        const placeHolder = this.width;
        this.width = this.height;
        this.height = placeHolder;
    }
    
    double(){
        this.width = this.width * 2;
        this.height = this.height * 2;
    }

}
module.exports = Rectangle;