function printSumArray(x) {
    var sum = 0;
    for(let i=0; i<x.length; i++) {
     sum = x[i] + sum;
    }
    return sum;
  }

console.log( printSumArray([1,3,-3]) ); // debería imprimir 6