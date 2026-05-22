
let n=74
let inverso=0
while (n>0){
    let digito=n%10
    inverso=inverso*10+digito
    n=(n-digito)/10
}
console.log("el numero invertido es :"+inverso)