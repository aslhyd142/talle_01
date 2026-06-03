let usuarios = [
    { nombre: "Ana", edad: 18 },
    { nombre: "Juan", edad: 15 },
    { nombre: "Laura", edad: 22 }
];

for (let i = 0; i < usuarios.length; i++) {
    if (usuarios[i].edad >= 18) {
        console.log(usuarios[i].nombre);
    }
}