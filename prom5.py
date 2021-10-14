a=0
b=1
c=0
n = int(input("ingrese el numero: "))
for i in range (0,n):
    c = a + b
    print(a,"+",b,"=",c)
    a=b
    b=c