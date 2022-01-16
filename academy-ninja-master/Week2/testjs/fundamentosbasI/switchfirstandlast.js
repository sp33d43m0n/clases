let x = [-2, 0, 3, -4, -1];
let y = [];
function firstandlast(x){
y[0]=x[0];
y[1]=x[x.length-1];
x[0]=y[0];
x[x.length-1]=y[1];
return x;
}

console.log(firstandlast(x));