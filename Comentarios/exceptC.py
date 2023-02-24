def try_syntax(numerator, denominator):                        # 1) Se denominala fución con sus parametros 
    try:                                                       # 2) Se inicia el bloque del codigo para dictar las excepciones
        print(f'In the try block: {numerator}/{denominator}')  # 3) Se imprime el mensaje remarcando los parametros dados al ejecutar la función incluso si presentan error
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator                       # 4) Variable donde se dicta el proceso en este caso matematico a ejecutar 
    except ZeroDivisionError as zde:                           # 5) Se escribe la excepción con su debido tipo de error que se quiere resaltar para su ejecución y cambiando su nombre a (zde)
        print(zde)                                             # 6) Se imprime la excepción
    else:                                                      # 7) Se utiliza else para que se ejecute cuando los parametros no presentan error
        print('The result is:', result)                        # 8) Se imprime el mensaje con la variable result
        return result                                          # 9)Se dicta que retorne la variable result aunque al ejcutarse lo mostrara en el ultimo lugar
    finally:                                                   # 10) Finally funciona para dictar la sentencia que finaliza el bloque de codigo
        print('Exiting')                                       # 11) Se imprime el mensaje que esta en finally
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 11))                                      # 12) Se imprime la función con los parametros (11,11) para mostrar el resultado de su ejecución