function returnOddArray(x){
    let oddnumber=[0];
    for (let i=1; i<=255; i+=2){
        oddnumber[i-1] = oddnumber.push(i);
    }
    oddnumber.shift();
    return oddnumber;
 }
 y = returnOddArray(255);
 console.log(y); // should log [1,3,5,...,253,255]