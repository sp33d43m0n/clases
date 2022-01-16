x = [1, 2, 3, 4, 5];
function moveahead(x){
    x.shift();
    x.push(0);
    console.log(x);
}

moveahead(x);

