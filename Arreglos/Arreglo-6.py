import random
v=[0,1]
r=round(random.random()*20-5)+5
r=int(input("Anote el rango en valor numerico "))
for i in range (2,r):
    v.append(v[i-1]+v[i-2])
print("rango",r)
print(v) 
if r>20:
    print("limite excedido maximo 20")
elif r<5:
    print("Minimo 5")
