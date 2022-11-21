import random
tam= random.randint(10,25) 
cont= 0
cont1=0
r=2
v1=tam%r!=0
v=[]
for i in range(tam):
    v.append(round(random.random()*100))
print(v)
for i in range(tam):
    while v[i]%r!=0:
        r+=1
    if v[i]==r:
        print(str(v[i])+"Es numero primo")
    else:
        print(str(v[i])+"No es primo")
            
    




 

