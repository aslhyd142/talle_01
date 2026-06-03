let votos = [
    "Ana",
    "Juan",
    "Ana",
    "Pedro",
    "Ana",
    "Juan"
];

let ana = 0;
let juan = 0;
let pedro = 0;

for (let i = 0; i < votos.length; i++) {
    if (votos[i] == "Ana") {
        ana++;
    } else if (votos[i] == "Juan") {
        juan++;
    } else if (votos[i] == "Pedro") {
        pedro++;
    }
}

console.log("Ana:", ana);
console.log("Juan:", juan);
console.log("Pedro:", pedro);

if (ana > juan && ana > pedro) {
    console.log("Ganador: Ana");
} else if (juan > ana && juan > pedro) {
    console.log("Ganador: Juan");
} else {
    console.log("Ganador: Pedro");
}