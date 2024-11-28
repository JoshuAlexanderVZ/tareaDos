num=int(input("Ingrese un nuemero: "))
a=0
b=1
c=0

for i in range (num):
    c=a+b
    a=b
    b=c
    fib_n=c

arriba = fib_n
while arriba > 1:
    primo_arriba = 1
    for i in range(2, arriba):
        if arriba % i == 0:
            primo_arriba = 0
            break
    if primo_arriba == 1:
        break
    arriba += 1

abajo = fib_n
while abajo > 1:
    primo_abajo = 1
    for i in range(2, abajo):
        if abajo % i == 0:
            primo_abajo = 0
            break
    if primo_abajo == 1:
        break
    abajo -= 1

if (fib_n - abajo) <= (arriba - fib_n):
    print(f"El número primo más cercano al índice {num} en Fibonacci es {abajo}")
else:
    print(f"El número primo más cercano al índice {num} en Fibonacci es {arriba}")

