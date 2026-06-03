numeros = []

for i in range(5):
    numeros.append(int(input("Número: ")))

sin_duplicados = []

for n in numeros:
    if n not in sin_duplicados:
        sin_duplicados.append(n)

print(sin_duplicados)