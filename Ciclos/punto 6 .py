c=0
max=0
n=int(input('ingrese numero negativo para parar'))
while n>=0:
    n=int(input('ingrese numero negativo para parar'))
    if n>=max:
        max= n
print("El número mayor es:",max)