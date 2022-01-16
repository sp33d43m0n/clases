let x = [2, 3, 4 ,20, 30, 9];
let y = 10;
let z = 0;

function biggerthany(x,y) {
for (let i=0; i<x.length; i++){
    if ( x[i] > y ) {
        z=z+1;
    }
    else {
        continue;
    }

}
console.log(z);
}

biggerthany(x,y);
