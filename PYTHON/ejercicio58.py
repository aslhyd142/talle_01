matriz = []

for i in range(3):
    fila = []

    for j in range(3):
        num = int(input("Número: "))
        fila.append(num)

    matriz.append(fila)

for fila in matriz:
    print(fila)