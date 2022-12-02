n = 999
cont = 0
for i in range(100, n + 1):
    p= True
    for j in range(100,i):
        if i == j:
           break
        elif i**j == 0:
           p = False
        else:
           continue
    if p == True:
        print(' ',i, end='')
        cont += 1
print('\nHay %u números sumas.' % cont )
    

#contadores y acumuladores
# var=var+constante 
#suma=suma + variable
   
    

