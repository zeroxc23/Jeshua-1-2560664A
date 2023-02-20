#Pida una cadena por teclado y diga cual es su valor al sumar sus codigos/
# Cual es el valor numerico de acuerdo a los códigos del alfabeto
def dig(a):
    list=[]
    suma=0
    for i in a:
        cod=ord(i)
        list.append(cod)
    for c in list:
        suma+=c   
    print(suma)
    print(list)
z=input('Ingrese valores al azar:')
dig(z)



