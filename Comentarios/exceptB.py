values = (2, 0)                             # 1) Se determina la variable que en este caso tiene 2 argumentos
#x,y=10,12
#print(divmod(10,3))
try:                                        # 2) Se inicia el bloque del codigo para dictar las excepciones
    q, r = divmod(*values)                  # 3) Se crea otra variable relacionandola con la primera con el uso de la función divmod()
    #print('valor de q=',q)
    print(f'q={q}')                         # 4) Se imprime el resultado del parametro q o "cociente" con el metodo de f string
    print(f'r={r}')                         # 5) Se imprime el resultado del parametro r o "residuo" con el metodo de f string
except (ZeroDivisionError, TypeError) as e: # 6) Se escribe la excepción con dos tipos de error que seran usados y simplificando a (e)
    print(type(e), e)                       # 7) Se imprime el mensaje imprimiendo el tipo de dato que es (e) 
