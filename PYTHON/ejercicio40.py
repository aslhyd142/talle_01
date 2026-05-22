numero=int(input("Ingrese un número: "))
inverso=0
while (numero>0):
    digito=numero%10
    inverso=inverso*10+digito
    numero=(numero-digito)//10

print("el numero invertido es :"+str(inverso))