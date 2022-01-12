x = [0, 3, -5, 10, -20, 0, 0, 10];

function removerange(low, high){
let conteo = high - low;    
x.splice(low,conteo);
return x;
}

console.log(removerange(2,5));






