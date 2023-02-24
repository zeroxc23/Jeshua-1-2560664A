def neg():
    try:
        num=int(input("Ingrese numero positivo o negativo:"))
        print(f" El {num} fue seleccionado")
        if num>=0:
            print(f"{num}/Es numero positivo")
        else:
            print(f"{num}/Es numero negativo")
    except ValueError as c:
        print(c)
        print("No es un valor numerico intente de nuevo")
        neg()
neg() 
