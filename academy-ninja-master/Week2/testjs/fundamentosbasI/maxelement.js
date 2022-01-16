
const x = [5,1,30,7];
var largestvalue = 0;

function largestelement(y) {
    for (let i = 0; i < y.length; i++)
    if (largestvalue > y[i]) {
        largestvalue = largestvalue;
    }
    else {
        largestvalue = y[i];
    }
    return largestvalue;
}



console.log( largestelement(x) );