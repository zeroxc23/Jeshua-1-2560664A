#Arreglo 1:
import random
def p(n):
    pro=0
    cont=0
    sum1=0
    tam=round(random.randrange(100))
    for i in range (tam):
        n.append(round(random.randrange(100)))
    for i in range(tam):
        cont+=1
        sum1+=n[i]
        pro=sum1//cont
        
    for i in range(tam):
        print("Promedio",pro)
        if n[i]==pro:
            print(n[i],"Es igual al promedio")
        elif n[i]<pro:
            print(n[i],"Es menor al promedio")
        else:
            print(n[i],"Es mayor al promedio") 
    return n
n=[]
a=p(n)
print(a)
