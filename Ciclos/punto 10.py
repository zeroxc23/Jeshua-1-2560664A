m=int(input("agregue primer numero"))
n=int(input("agregue segundo numero"))
while n!=0:
        r=m%n
        m=n
        n=r
    
print((m,n))