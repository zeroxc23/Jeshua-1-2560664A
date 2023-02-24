try:                               # 1) Inicio del bloque de codigo para ejecutar las excepciones
    #print(1/1))
    raise SyntaxError              # 2) Se utiliza para generar el error de la manera que decidimos
except SyntaxError as e:           # 3) Se escribe la excepción con su debido tipo de error que se quiere resaltar para su ejecución y cambiando su nombre a (e)
    print(e)                       # 4) Se imprime la excepción (e)
    print('Cierra el parentesis')  # 5) Se imprime el mensaje
#--------------------------------------------------------------------------------------------------------------
try:                               # 1) Inicio del bloque de codigo para ejecutar las excepciones
    #raise ZeroDivisionError
    print(1/0)                     # 2) Se imprime el resultado de lo estipulado en el parentesis
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:   # 3) Se escribe la excepción con su debido tipo de error que se quiere resaltar para su ejecución y cambiando su nombre a (zde)
    
    print(zde)                     # 4) Se imprime la excepción llamada (zde)
    #print('prueba error')