numeros = []

for i in range(5):
    numeros.append(int(input("Número: ")))

mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print("Mayor:", mayor)