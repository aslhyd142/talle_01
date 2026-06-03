let N = 5;
let arreglo = [];
let suma = 0;

for (let i = 0; i < N; i++) {
    arreglo[i] = Math.floor(Math.random() * 100) + 1;
    suma += arreglo[i];
}

console.log(arreglo);
console.log("Suma =", suma);