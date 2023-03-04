class Aprendiz:                              # Se define o crea la clase aprendiz
    def __init__(self,nombre):               # Se define el constructor con sus parametros
        self.__nombre=nombre                 # Se define el atributo relacionando con el parametro nombre
        self.__cursos=[]                     # Se define el atributo con la lista cursos
    def agregarCurso(self,nombreCurso):      # Se define el metodo agregar curso con el parametro nombreCurso
        self.__cursos.append(nombreCurso)    # Agrega en la lista cursos el parametro nombreCurso
    def verCursos(self):                     # Se define el metodo verCursos
        return self.__cursos                 # Retorna cursos

class Curso:                                 # Se define la clase curso
    def __init__(self,nombreCurso):          # Se define el constructor 
        self.__nombreCurso=nombreCurso       # Se define el atributo relacionando con el parametro nombreCurso
    def getNombreCurso(self):                # Se define el metodo getNombreCurso
        return self.__nombreCurso            # Retorna nombreCurso
    
ob=Aprendiz('Miguel')                        # Se define el objeto de la clase aprendiz
c1=Curso('Python Basico')                    # Se define el objeto de la clase curso
c2=Curso('Python Intermedio')                # Se define el objeto de la clase curso
c3=Curso('Java Basico')                      # Se define el objeto de la clase curso

ob.agregarCurso(c1)                          # Se invoca el metodo agregarCurso con el objeto c1 en relación con el objeto ob
ob.agregarCurso(c2)                          # Se invoca el metodo agregarCurso con el objeto c2 en relación con el objeto ob
ob.agregarCurso(c3)                          # Se invoca el metodo agregarCurso con el objeto c3 en relación con el objeto ob

for curso in ob.verCursos():                 # Se usa un for que recorra curso en relación al objeto con el metodo VerCursos
    print(curso.getNombreCurso())            # Imprime el mensaje

del ob                                       # Se elimina el objeto ob
#print(ob)
print('.....',c1.getNombreCurso())           # Imprime el mensaje

