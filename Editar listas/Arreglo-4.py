import random
a=int(0)
nah=random.randint(10,25)
v=[(round(random.random()*100)) for i in range(nah)]

print("desorden",v)
print("Total de numeros",v.__len__())

a=False
b=False
while a==False:
    a=True
    for i in range (len(v)-1):
        if v[i]>v[i+1]:
            h=v[i]
            v[i]=v[i+1]
            v[i+1]=h
            a=False

print("orden menor a mayor",v)

while b==False:
    b=True
    for a in range(len(v)-1):
        if v[a]<v[a+1]:
            c=v[a]
            v[a]=v[a+1]
            v[a+1]=c
            b=False

print("de mayor a menor",v)
