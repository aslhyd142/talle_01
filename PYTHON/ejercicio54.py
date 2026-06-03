usuarios = []

for i in range(3):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    usuarios.append([nombre, edad])

for usuario in usuarios:
    if usuario[1] >= 18:
        print(usuario[0])