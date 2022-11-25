#libro:Python 3 curso practico
#Pagina:127
suma=0
for i in range(10):
    if i>7:
        break
    suma=suma+i
print("La suma con break ha sido:",suma)
for i in range(10):
    suma=suma+i
print("La suma sin break ha sido:",suma)
