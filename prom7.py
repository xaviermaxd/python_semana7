par=0
impar=0
n=int(input("ingrese la cantidad de numeros: "))
for i in range(n):
    num = int(input("ingrese el numero: "))
    if num % 2 == 0:
            par += num
    else:
        impar += num
print("la suma de pares es: ",par)
print("la suma de impares es: ", impar)