import random
def sic(v):
    tam= random.randint(10,25)
    sum=0
    pro=0
    mod=[]
    dmod={}
    for i in range(tam):
        v.append(round(random.random()*100))
    print(v)
    fm=0
    nr=v[0]
    print(dmod)
    cont1=0
    for numero in v:
        c1=str(numero)
        if not c1 in dmod:
            dmod[c1]=1
        else:
            dmod[c1]+=1
            for numero in dmod:
                if dmod[numero]>fm:
                    nr=numero
                    fm=dmod[numero]
                cont1 = dmod[str(nr)]

            print("La moda es :",nr)
v=[]
b=sic(v)
print(b)