function returnOddArray(x){
    let oddnumber=[];
    let i=1;
    for (let k=0; k<255; k++){
        oddnumber.push(i);
        i=i+2;
    }
    // oddnumber.shift();
    return oddnumber;
 }
 y = returnOddArray(255);
 console.log(y); // should log [1,3,5,...,253,255]