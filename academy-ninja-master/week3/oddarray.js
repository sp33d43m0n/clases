function returnOddArray(x){
    let oddnumber=[0];
    for (let i=1; i<=255; i+=2){
        oddnumber[i-1] = oddnumber.push(i);
    }
    /oddnumber.shift();  line to kill 2/
    return oddnumber;
 }
 y = returnOddArray(255);
 console.log(y); // should log [1,3,5,...,253,255]

//  el valor i-1 es por que quiero que comience en la posicion cero del array