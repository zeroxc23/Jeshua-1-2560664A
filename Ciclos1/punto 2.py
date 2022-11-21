n=int(input("digite numero"))
r=2
while n % r!=0:
    r+=1
if r==n:
    print(str(n)+"es numero primo")
else:
    print(str(n)+"no es numero primo")
