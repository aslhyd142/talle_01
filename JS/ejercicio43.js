 let numeros = [12, 8, 25, 4, 18];

let mayor = numeros[0];

for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] > mayor) {
        mayor = numeros[i];
    }
}

console.log("Mayor =", mayor);