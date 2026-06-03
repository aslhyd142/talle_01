notas = []
suma = 0

for i in range(5):
    nota = float(input("Nota: "))
    notas.append(nota)
    suma += nota

promedio = suma / 5

print("Promedio:", promedio)

if promedio >= 3:
    print("Aprobado")
else:
    print("Reprobado")