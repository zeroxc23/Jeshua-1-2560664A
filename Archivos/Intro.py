flujo=open('archivos/inicio.txt','a')               #Se determina la variable con el metodo open con la ruta relativa y el modo a de agregación
#datos=flujo.read()
#print(datos)
flujo.write('\nCuando estudian con juicio')        # Se utiliza el metodo write para editar el archivo de la ruta
datos=flujo.read()                                 # Se determina la variable datos con el metodo read para que lea el archivo
print(datos)                                       # Imprime el mensaje