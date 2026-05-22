// Generar número aleatorio entre 1 y 10
const numeroSecreto = Math.floor(Math.random() * 10) + 1;

let intento = 0;

console.log("Adivina el número entre 1 y 10");

while (intento !== numeroSecreto) {

intento = 2;

    if (intento === numeroSecreto) {
        console.log("¡Correcto! Adivinaste el número.");
    } else if (intento > numeroSecreto) {
        console.log("El número a adivinar es mayor.");
        break;
    } else {
        console.log("El número a adivinar es menor.");
        break;
    }
}