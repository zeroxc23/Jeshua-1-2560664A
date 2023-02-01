
def mas(a):
    i=1
    total=0
    while(i<a):
        if a%i==0:
            total=total+i
        i=i+1
    if total==a:
        print("el numero es perfecto:", a)
    else:
        print("no es perfecto", a )

def divi(a):
    for i in range (1,a):
        if a%i==0:
            print("sus divisiores son",i)
def rang(a):
    for i in range (a):
        if i%5==0:
            print(i,"multiplo de 5")
        else:
            print(i,"no es multiplo de 5")
def pot(a,b):
    c=1
    potencia=a
    while(c<b):
        c+=1
        potencia*=a
    if b<=0:
        potencia=1
    print(potencia)      
def linea(a):
    for i in range (a):
        print("*"*(i+1))