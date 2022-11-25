#libro:Python 3 curso practico
#Pagina: 127
suma=0
print("El programa ira pidiendo numeros y los ira sumando hasta que la suma super el valor 100")
while True:
    numero=eval(input("Introduce un numero"))
    suma=suma+numero
    if suma>100:
        break
print("La suma total al superar los 100 son:",suma)