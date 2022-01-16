let x = [0, -5, -20, 10 , 0, 34];
let y = 0;

function maxminave(x){
    let min=0;
    let max=0;
    let sum=0;
    for (let i=0; i<x.length; i++){
        if (max<x[i])  {
            sum = sum + x[i]; 
            max = x[i]; 
            }
        else if (min > x[i]) { 
            sum = sum + x[i]; 
            min = x[i];
        }
    }
return [max,min,sum/x.length];
}


console.log(maxminave(x));

