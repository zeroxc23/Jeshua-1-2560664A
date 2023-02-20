#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última
def sub(a):
    c=len(a)
    for i in range(1,c):
        print(a[0:i+1])
x=input("Ingrese una palabra al azar:")
sub(x)