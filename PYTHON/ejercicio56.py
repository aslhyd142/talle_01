total = 0

cantidad = int(input("Cantidad de productos: "))

for i in range(cantidad):
    producto = input("Producto: ")
    precio = float(input("Precio: "))

    total += precio

print("Total a pagar:", total)