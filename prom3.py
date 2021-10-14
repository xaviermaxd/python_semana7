n = int(input("ingrese la cantidad de numeros: "))
suma = 0
for i in range (n):
    num = int(input("numero: "))
    suma += num
    prom = suma/n
print ("la suma es: ",suma)
print ("el promedio es: ",prom)