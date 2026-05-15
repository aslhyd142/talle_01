nota=float(input("ingrese la nota: "))
if(nota>=4.5 or nota==5):
    print("Aprobado")
elif(nota>=4 and nota<=4.49):
    print("Regular")
elif(nota>=3 and nota<=3.99):
    print("Insuficiente")
else:
    print("Reprobado")
