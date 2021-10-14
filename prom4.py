par = 0
impar = 0
for i in range (6):
    num = int(input("ingrese el numero: "))
    if num % 2 ==0:
        par += 1
    else:
        impar += 1
print("la cantidad de numeros pares es: ",par)
print("la cantidad de numeros impares es: ",impar)