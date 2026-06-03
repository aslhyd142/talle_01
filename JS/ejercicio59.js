let secreto = 7;
let intentos = [3, 5, 7, 2, 1];

let ganador = false;

for (let i = 0; i < 5; i++) {
    if (intentos[i] == secreto) {
        console.log("Adivinaste en el intento", i + 1);
        ganador = true;
        break;
    }
}

if (!ganador) {
    console.log("Perdiste");
}