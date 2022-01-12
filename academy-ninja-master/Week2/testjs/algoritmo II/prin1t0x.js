function printUpTo(x) {
    if (x > 0) {
    for (let i = 0; i<=x; i+=2)
    console.log(i);
  }
  else
  return "false";
}
  printUpTo(1000); // debería imprimir todos los enteros de 1 to 1000
  y = printUpTo(-10); // debería imprimir false
  console.log(y); // debería imprimir false