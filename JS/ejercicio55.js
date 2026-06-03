let numeros = [10, 5, 20, 8, 15];

let mayor = numeros[0];
let menor = numeros[0];
let suma = 0;

for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] > mayor) {
        mayor = numeros[i];
    }

    if (numeros[i] < menor) {
        menor = numeros[i];
    }

    suma += numeros[i];
}

let promedio = suma / numeros.length;

console.log("Mayor:", mayor);
console.log("Menor:", menor);
console.log("Promedio:", promedio);