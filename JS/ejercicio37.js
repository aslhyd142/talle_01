n=24
fibonacci=0
fibonacci1=1
for (i = 1; i <= n; i++){
    console.log("fibonacci: " + fibonacci);
    fibonacci2 = fibonacci + fibonacci1;
    fibonacci = fibonacci1;
    fibonacci1 = fibonacci2;
}