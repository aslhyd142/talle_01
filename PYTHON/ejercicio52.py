personas = ["Ana", "Juan", "Pedro"]

nuevo = input("Agregar nombre: ")
personas.append(nuevo)

print(personas)

personas[0] = input("Nuevo nombre para posición 0: ")

print(personas)

personas.pop(1)

print(personas)