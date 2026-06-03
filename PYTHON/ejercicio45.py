numeros = []
suma = 0

for i in range(5):
    n = int(input("Número: "))
    numeros.append(n)
    suma += n

promedio = suma / len(numeros)

print("Promedio:", promedio)