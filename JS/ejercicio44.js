let numeros = [12, 8, 25, 4, 18];

let menor = numeros[0];

for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] < menor) {
        menor = numeros[i];
    }
}

console.log("Menor =", menor);