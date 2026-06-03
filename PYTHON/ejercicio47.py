numeros = []

for i in range(5):
    numeros.append(int(input("Número: ")))

buscar = int(input("Número a buscar: "))

if buscar in numeros:
    print("Posición:", numeros.index(buscar))
else:
    print("No existe")