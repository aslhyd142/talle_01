ana = 0
juan = 0
pedro = 0

cantidad = int(input("Cantidad de votos: "))

for i in range(cantidad):
    voto = input("Vote por Ana, Juan o Pedro: ")

    if voto == "Ana":
        ana += 1
    elif voto == "Juan":
        juan += 1
    elif voto == "Pedro":
        pedro += 1

print("Ana:", ana)
print("Juan:", juan)
print("Pedro:", pedro)

if ana > juan and ana > pedro:
    print("Ganador: Ana")
elif juan > ana and juan > pedro:
    print("Ganador: Juan")
else:
    print("Ganador: Pedro")