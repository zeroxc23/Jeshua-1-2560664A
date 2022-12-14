import random
tam=random.randint(10, 25)
pro=0
cont=0
sum = 0
v = [(round(random.random()*100)) for i in range(tam)]
for i in range(tam):
    cont+=1
    sum+=v[i]
    pro=sum//cont
print(v)
print("Total de numeros",cont)
print("Promedio",pro)
print("suma total",sum)
for i in range(len(v)):
    if v[i]==pro:
        print("-",v[i],"El es igual al promedio")
    elif v[i]<pro:
        print("-",v[i],"Es menor al promedio")
    else:
        print("-",v[i],"El valor es mayor al promedio")
