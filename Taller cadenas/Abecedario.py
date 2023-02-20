#Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
def let(pe):
    cont=0
    numb=''
    for i in pe:
        if i not in numb:
            numb+=i
    return len(numb)
sa=input("Ingrese una palabra al azar:")
print(let(sa))

        
