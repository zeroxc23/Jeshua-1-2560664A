def num (a,b):
    c=1
    potencia=a
    while(c<b):
        c+=1
        potencia*=a
    if b<=0:
        potencia=1
    print(potencia)
num(2,4)
