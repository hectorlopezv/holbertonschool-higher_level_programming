#!/usr/bin/node
//hola
exports.nbOccurences = function (list, element) {
    const exist = list.includes(element);
    let NumberAp = 0;
    
    if(!exist){
        console.log(NumberAp);
        return;
    }

    list.forEach( number => {
        if(number === element){
            NumberAp += 1;
        }
    });
    return NumberAp;
}