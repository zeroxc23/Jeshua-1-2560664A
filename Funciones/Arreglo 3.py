import random

def D(num):
    tam=random.randint(10,25)
    cont2=0
    cont1=0
    sum1=0
    sum2=0
    
    for i in range (tam):
        num.append(round(random.random()*100))
    print(num)
    for i in range(tam):
        if num[i]%2==0:
            cont1=cont1+1
            sum1+=num[i]
            print(num[i],"Par")
        elif num[i]!=0:
            cont2=cont2+1
            sum2+=num[i]
            print(num[i],"Impar")
        print("Total de pares:",cont1)
        print("Total de impares:",cont2)
        print("Suma par",sum1)
        print("Promedio impar",sum2//cont2)
 
num=[]
b=D(num)
print(b)
    

