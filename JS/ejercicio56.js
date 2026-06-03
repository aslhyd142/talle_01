let carrito = [];
let total = 0;

carrito.push({ producto: "Mouse", precio: 50000 });
carrito.push({ producto: "Teclado", precio: 80000 });

for (let i = 0; i < carrito.length; i++) {
    total += carrito[i].precio;
}

console.log(carrito);
console.log("Total:", total);