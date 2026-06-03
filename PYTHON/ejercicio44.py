numeros = []

for i in range(5):
    numeros.append(int(input("Número: ")))

menor = numeros[0]

for n in numeros:
    if n < menor:
        menor = n

print("Menor:", menor)