salariobase=int(input("ingrese el salario base: "))
horas=int(input("ingrese el numero de horas trabajadas: "))
valorhora=int(input("ingrese el valor de la hora: "))
horas_extra= horas*(1.5 * valorhora)

salario_total=horas_extra+salariobase
print("salario total:"+ str(salario_total))