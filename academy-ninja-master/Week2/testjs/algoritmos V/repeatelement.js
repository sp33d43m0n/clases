x = [-2, 0, "casa", -4, -1];
let y = [];
let k = 0;

function repeatelement(x){
for (var i=0; i<x.length; i++){
    y[k]=x[i];
    y[k+1]=x[i];
    k=k+2;
}
console.log(y);
}

repeatelement(x);