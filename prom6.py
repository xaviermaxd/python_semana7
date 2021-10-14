par=0
impar=0
posi=0
nega=0
neutro=0
for num in range(5):
    num = int(input("ingrese el numero:"))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    
    if num < 0 :
        nega += 1
    elif num == 0 :
        neutro += 1
    else:
        posi += 1
print("la cantidad de pares es:",par)
print("la cantidad de impares es:",impar)
print("la cantidad de positivos es:",posi)
print("la cantidad de negativos es:",nega)
print("la cantidad de neutros es:",neutro)