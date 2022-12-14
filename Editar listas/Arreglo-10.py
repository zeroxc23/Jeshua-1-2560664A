from cmath import sqrt
import random
tam= random.randint(10,25) 
cont= 0
sum1=0
v=[(round(random.random()*100)) for i in range(tam)]

print(v)
mean = sum1 / len(v)
re = sum((l-mean)**2 for l in v) / len(v)
d = sqrt(re)

print("desviacion estandar ",d)