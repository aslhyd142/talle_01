salario=4500000
if (salario<1500000){
    console.log("impuesto del 0%")
    netosalario=salario-(salario*0)
    console.log("el salario neto es:" + netosalario)
}
else if (salario <=3000000){
    console.log("impuesto del 10%")
    netosalario=salario-(salario*0.10)
    console.log("el salario neto es:" + netosalario)
}
else if (salario>3000000 ){
    console.log("impuesto del 20%")
    netosalario=salario-(salario*0.20)
    console.log("el salario neto es:" + netosalario)
}