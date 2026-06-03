let contraseña = "clave123";

let tieneNumero = false;

for (let i = 0; i < contraseña.length; i++) {
    if (!isNaN(contraseña[i]) && contraseña[i] !== " ") {
        tieneNumero = true;
    }
}

if (contraseña.length >= 8 && tieneNumero) {
    console.log("Contraseña válida");
} else {
    console.log("Contraseña inválida");
}