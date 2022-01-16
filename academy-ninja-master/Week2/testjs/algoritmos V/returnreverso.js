let x = [-2, 0, 3, -4, -1];
let y = [];
function returnreverso(x){
for (let i = 0; i <x.length; i++){
    y[i]= x[(x.length-1)-i];
}
console.log(y);
}

returnreverso(x);
