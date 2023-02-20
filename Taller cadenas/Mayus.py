#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas
def let(x):
    print("Todo en mayuscula:",x.upper())
    print("Todo en minuscula:",x.lower())
    print("Solo primera letra en mayuscula:",x.capitalize())
chain=str(input("Ingrese letras al azar alternando entre mayuscula y minuscula:"))
let(chain)