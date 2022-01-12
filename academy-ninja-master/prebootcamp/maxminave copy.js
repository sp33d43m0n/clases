let x = [2, 20, -5, 1 , 0, -2];
let y = 0;

function maxminave(x){
    let min=0;
    let max=0;
    let sum=0;
    for (let i=0; i<x.length; i++){
        if (x[i] >= max){  
            sum = sum + x[i];
            if (max < min){
            min = max;
            }
            max = x[i]; 
        }
        else if (x[i] <= min) {
            sum = sum + x[i];
            min = x[i];
        }
        else {
            sum= sum + x[i];
            continue;
        }
          
        }
        return [max,min,sum]    
}

console.log(maxminave(x));

