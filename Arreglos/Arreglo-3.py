import random
tam=random.randint(10,25)
cont2=0
cont1=0
sum1=0
sum2=0
vector=[]
for i in range (tam):
    vector.append(round(random.random()*100))
print(vector)

for i in range(tam):
    if vector[i]%2==0:
        cont1=cont1+1
        sum1+=vector[i]
        print(vector[i],"Par")
    else:
        cont2=cont2+1
        sum2+=vector[i]
        print(vector[i],"Impar")

print("Total de pares:",cont1)
print("Total de impares:",cont2)
print("Suma par",sum1)
print("Promedio impar",sum2//cont2)
