class Curso:                                  # Se define o crea la clase curso
    def __init__(self,titulo):                # Se define el constructor con sus parametros
        self.__titulo=titulo                  # Se define el atributo en relación con el parametro titulo

    def getTitulo(self):                      # Se define el metodo getTitulo
        return self.__titulo                  # Retorna titulo

class Aprendiz:                               # Se define o crea la clase aprendiz
    def __init__(self,nombre):                # Se define el constructor con sus parametros
        self.__nombre=nombre                  # Se define el atributo en relación con el parametro nombre
        self.__cursos=[]                      # Se define el atributo con la lista cursos

    def agregarCurso(self,nombreCursito):     # Se define el metodo agregarCurso
        cursito=Curso(nombreCursito)          # Se define el objeto dentro del metodo
        self.__cursos.append(cursito)         # Agrega en la lista cursos el parametro cursito

    def getCursos(self):                      # Se define el metodo getCursos
        return self.__cursos                  # Retorna cursos
    
ap=Aprendiz('Sofia')                          # Se define el objeto de la clase aprendiz
ap.agregarCurso('Python Basico')              # Se invoca el metodo agregarCurso con el objeto ap
ap.agregarCurso('Python Intermedio')          # Se invoca el metodo agregarCurso con el objeto ap

for c in ap.getCursos():                      # Hace un recorrido de c en el objeto ap con el metodo getCursos
    print(c.getTitulo())                      # Imprime el mensaje  
 
del ap                                        # Borra el objeto ap
