from re import X


a=int(input("digite el numero base"))
b=int(input("agregue el exponente"))
c=1
potencia=a
while(c<b):
    c+=1
    potencia*=a
    if b<=0:
        potencia=1
    print(potencia)

