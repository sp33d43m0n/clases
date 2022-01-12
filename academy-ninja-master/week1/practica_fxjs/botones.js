// Usamos ID en html para extraer datos del html y con document.getElementById podemos extraer los datos del html
let btn = document.getElementById('btn');

// function querico(msg) {
//     alert(`Hola como estas ${msg}`)
// }

// Funcion para escuchar el evento y se coloca click como el evento a detectar.

btn.addEventListener('click', () => {
    let txtresult = document.getElementById('txtresult');
    let msg = document.getElementById('message').value;
    // alert(msg);
    txtresult.innerHTML = msg;
})

