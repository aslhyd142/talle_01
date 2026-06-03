let numeros = [10, 20, 30, 40, 50];
let buscar = 30;

let posicion = -1;

for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] == buscar) {
        posicion = i;
        break;
    }
}

if (posicion != -1) {
    console.log("Posición =", posicion);
} else {
    console.log("No existe");
}