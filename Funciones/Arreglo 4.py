from ast import Nonlocal
import random
def cox(n):
    tam= random.randint(10,25)
    sum=0
    cont=0
    for i in range(tam):
        n.append(round(random.random()*100))
    print(n)
    for i in range (tam):
        cont+=1
        sum+=n[i]
    print("Cantidad de numeros",cont)
    print("Suma total",sum)
    print("Promedio",sum//cont)
n=[]
b=cox(n)
print(b)