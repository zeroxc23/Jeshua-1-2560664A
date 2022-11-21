n=int(input("ingrese numero"))
i=1
total=0
while(i<n):
    if n%i==0:
        total=total+i
    i=i+1


if total==n:
    print("el numero es perfecto:", n)
else:
    print("no es perfecto", n )
     




    