import random
tam= random.randint(10,25) 
cont= 0
cont1=0
r=2
v1=tam%r!=0
v=[(round(random.random()*100)) for i in range(tam)]
print(v)
for n in range(tam):
   v.append(round(random.random()*100))
print("lista",v)
for n in v:
    i=1
    cont=0
    while(n>=i):
        if n%i==0:
            cont+=1
        i+=1
    if not cont>2 or n <=1:
        print(n,"Es numero primo")
            
    




 

