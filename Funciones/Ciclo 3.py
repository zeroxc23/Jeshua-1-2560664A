def pri(n):
    r=2
    while n % r!=0:
        r+=1
    if r==n:
        print(str(n) + "es numero primo")
    else:
        print(str(n) + "no es numero primo")
pri(7)