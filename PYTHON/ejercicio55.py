numeros = []
suma = 0

for i in range(5):
    n = int(input("Número: "))
    numeros.append(n)
    suma += n

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

    if n < menor:
        menor = n

print("Mayor:", mayor)
print("Menor:", menor)
print("Promedio:", suma / len(numeros))