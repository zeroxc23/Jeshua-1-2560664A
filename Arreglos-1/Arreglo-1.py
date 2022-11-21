import random
tam=random.randint(10, 25)
pro=0
cont=0
sum = 0
v = []
for i in range(tam):
    v.append(round(random.random()*100))
    cont+=1
    sum+=v[i]
    pro=sum//cont
print(v)
print("Promedio",pro)
for i in range(len(v)):
    if v[i]==pro:
        print("-",v[i],"El es igual al promedio")
    elif v[i]<pro:
        print("-",v[i],"Es menor al promedio")
    else:
        print("-",v[i],"El valor es mayor al promedio")