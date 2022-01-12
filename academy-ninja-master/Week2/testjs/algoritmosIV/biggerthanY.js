let x = [2, 3, 4 ,20, 30, 9];
let y = 10;


function biggerthany(x,y) {
for (let i=0; i<x.length; i++){
    if ( x[i] > y ) {
        console.log(x[i]);
    }
    else {
        continue;
    }

}

}

biggerthany(x,y);
