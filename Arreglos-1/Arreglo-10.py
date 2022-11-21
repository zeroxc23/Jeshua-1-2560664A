from cmath import sqrt
import random
tam= random.randint(10,25) 
cont= 0
sum1=0
v=[]
for i in range(tam):
    v.append(round(random.random()*100))
print(v)
mean = sum1 / len(v)
re = sum((l-mean)**2 for l in v) / len(v)
d = sqrt(re)

print("desviacion estandar ",d)