tipodecliente=int(input("ingrese el tipo de cliente: "))


if(tipodecliente==1):
    print("el cliente es vip: 0.20 de descuento")
elif(tipodecliente==2):
    print("el cliente es normal: 0.05 de descuento")
else:
    print("cliente no registrado en el sistema")
