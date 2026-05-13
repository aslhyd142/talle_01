salario=int(input("salario:"))
if salario<1500000:
    print("impuesto del 0%")
    netosalario=salario-(salario*0)
    print("el salario neto es:", + netosalario)

elif salario <=3000000:
    print("impuesto del 10%")
    netosalario=salario-(salario*0.10)
    print("el salario neto es:", + netosalario)

else: salario>3000000
print("impuesto del 20%")
netosalario=salario-(salario*0.20)
print("el salario neto es:", + netosalario)
