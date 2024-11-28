num=int(input("Ingrese un nuemero: "))
a=0
b=1
c=0
cont=0
fin=1
while fin==1:
    if num==c:
        print("Su numero está dentro de la suceción, y es el numero", cont)
        fin-=1
    elif c>num:
        print("Su numero no pertenece al sucecion")
        fin-=1
    else:
        c=a+b
        a=b
        b=c
        cont+=1


