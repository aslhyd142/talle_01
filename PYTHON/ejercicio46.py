numeros = []
pares = 0

for i in range(5):
    n = int(input("Número: "))
    numeros.append(n)

for n in numeros:
    if n % 2 == 0:
        pares += 1

print("Cantidad de pares:", pares)