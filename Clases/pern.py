class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre
    def getdocum(self):
        return self.__documento

    def setNombre(self,nombre):
        self.__nombre=nombre
    def docum(self,documento):
        self.__documento=documento
class aprendiz(Persona):
    def __init__(self,ficha,nombre,documento):
        Persona.__init__(self,nombre,documento)
        self.__ficha=ficha
    def getficha(self):
        return self.__ficha        
    def gettodo(self):
        print("Documento",app.getdocum())
        print("Ficha",app.getNombre())
        print("Nombre",app.getficha())
app=aprendiz("luis",11212,12354)
print(app.gettodo())