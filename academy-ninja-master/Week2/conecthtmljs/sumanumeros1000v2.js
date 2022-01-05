function sum_odd_5000(){
    let sum = 0;
    for (let i=1; i<=1000; i++){
        //residuo = i%2;
        if (i%2 === 0){
            sum = sum + i;
        }
    } 
    return sum;
}

z= sum_odd_5000();
console.log(z);