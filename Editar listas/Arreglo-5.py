import random
tam=int(input("Anote el rango para aivinar el numero "))
n=int(input("Adivine el numero escriba:"))
v=[(round(random.random()*100)) for i in range(tam)]
po=[]
ve=0
for i in range(tam):
    v.append(round(random.random()*100))
print("Lista",v)
if n==v[i]:
    print("Coincide con la lista",n)
else:
    v.append(n)
    
    print("No coincide",v)
for i in range (len(v)):
    if n==v[i]:
        ve+=1
        po.append(i)
if ve>0:
    print("El numero se repite:",ve,"\nLas posiciones son:",po)
