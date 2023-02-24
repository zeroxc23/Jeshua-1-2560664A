def err(o):
    try:
        assert o>200 and o<300
    except AssertionError:
        print(f"El valor:{o}/no entra en el rango")
    else:
        print(f"El valor:{o}/entra en el rango")
o=int(input("Ingrese un numero al azar:"))
err(o)