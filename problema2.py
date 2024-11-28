a= int(input("Ingrese un numero: "))
b= int(input("Ingrese otro numero: "))
c=0

for i in range (10):
    c=a+b
    a=b
    b=c
    print(c)