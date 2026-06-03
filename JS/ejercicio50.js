let numeros = [1, 2, 3, 2, 4, 1, 5];
let nuevo = [];

for (let i = 0; i < numeros.length; i++) {
    if (!nuevo.includes(numeros[i])) {
        nuevo.push(numeros[i]);
    }
}

console.log(nuevo);