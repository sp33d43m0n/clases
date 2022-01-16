function printSum(x) {
    var sum = 0;
    for (let i = 1; i<=x; i+=2){
        sum = sum + i;
       
    }
    return sum
  }
  y = printSum(1000) // debería imprimir todos los imparesde 1 a 10000 
  console.log(y)  