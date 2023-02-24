def edad():                                             # 1) Se denomina la función con el espacio del parametro vacio
    try:                                                # 2) Se inicia el bloque de codigo
        tuedad=int(input("introduce tu edad"))          # 3) Se denomina la variable (tuedad) con las caracteristicas que el usuario escriba la edad recalcando que 
                                                        # sea valores numericos enteros 
        print(f'tu edad es  {tuedad}')                  # 4) Se imprime la variable tuedad con el metodo f string 
        #print('Tu edad es ',tuedad)
    except ValueError as e:                             # 5) Se escribe la excepción con su error definido cambiando su nombre a (e)
        print(e)                                        # 6) Se imprime la excepción llamada (e)
        print("La edad debe ser un valor numerico...")  # 7) Se imprime el mensaje
        edad()                                          # 8) Se invoca la fucnión por si se equivoca o no hay nada repita la fucnión hasta anotar los valores correctos 
    
edad()                                                  # 9) Se invoca la función para su debida ejecución  