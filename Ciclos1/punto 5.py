#¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000? 
n = 1000
cont = 0
for i in range(2, n + 1):
    p= True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           p = False
        else:
           continue
    if p == True:
        print(' ',i, end='')
        cont += 1
print('\nHay %u números primos.' % cont )

