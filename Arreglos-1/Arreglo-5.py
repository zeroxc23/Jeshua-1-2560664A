import random
n=int(input("Adivine el numero escriba:"))
tam=int(input("Anote el radngo para aivinar el numero "))
v=[]
for i in range(tam):
    v.append(round(random.random()*100))
print(v)
if n==v[i]:
    print("Coincide con la lista",n)
else:
    v.append(n)
    
    print("No coincide",v)