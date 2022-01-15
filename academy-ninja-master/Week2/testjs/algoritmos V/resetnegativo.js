let x=[-1, 0, -23, 3, 3, 4];

function resetnegativo(x) {

    for (let i=0; i<=x.length; i++){
        if (x[i]<0) {
            x[i]=0;
        }
    }
    return x;
}

console.log(resetnegativo(x));