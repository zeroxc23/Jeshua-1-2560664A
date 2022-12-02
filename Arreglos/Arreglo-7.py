import random
from statistics import mode
tam= random.randint(10,25)
sum=0
cont=0
v=[]
for i in range(tam):
    v.append(round(random.random()*100))
print(v)
for i in range (tam):
    cont+=1
    sum+=v[i]


print("Cantidad de numeros",cont)
print("Suma total",sum)
print("Promedio",sum//cont)