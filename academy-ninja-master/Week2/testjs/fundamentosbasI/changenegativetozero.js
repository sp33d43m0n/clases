x = [-2, 0, 3, -4, -1];

function changenegativetodojo(x){
for (let i = 0; i < x.length; i++) {
    if (x[i] < 0){
        x[i] = 0;
    }
}
return x;
}

console.log(changenegativetodojo(x));




