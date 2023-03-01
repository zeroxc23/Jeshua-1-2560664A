class Persona:                                     #Se define o crea la clase llamada persona
    def __init__(self,nombre,documento):           #Se define el metodo del constructor con sus parametros
        self.__nombre=nombre                       #Se define el atributo relacionando con el parametro nombre
        self.__documento=documento                 #Se define el atributo relacionando con el parametro documento 
        #print('Constructor Activado')        

    def getNombre(self):                           #Se define el metodo getnombre para que realize el proceso con el nombre ingresado
        return self.__nombre                       #Devuelve el atributo nombre para imprimirlo incluso estando privado

    def getdocum(self):                            #Se define el metodo getdocum para que que realice el proceso del numero de documento ingresado 
        return self.__documento                    #Devuelve el atributo documento para imprimirlo incluso estando privado
    def setNombre(self,nombre):                    #Se define el metodo setNombre para que realice el proceso con el nombre ingresado/de momento no se llama
        self.__nombre=nombre                       #Se define el atributo relacionando con el parametro nombre/de momento no se llama 
    def docum(self,documento):                     #Se define el metod docum para que realice el proceso con el parametro documento
        self.__documento=documento                 #Se define el atributo relacionando con el parametro documento 
class aprendiz(Persona):                           #Se define la herencia aprendiz determinando la relación con la clase padre persona
    def __init__(self,nombre,documento,ficha,):     #Se define el metodo del constructor con sus parametros y uno nuevo que es ficha
        self.__ficha=ficha                         #Se define el atributo relacionando con el parametro ficha
        Persona.__init__(self,nombre,documento)    #Se realiza un init para relacionar los parametros con la clase padre
    def getficha(self):                            #Se define el metodo getficha para que realice el proceso del numero de ficha ingresado
        return self.__ficha                        #Devuelve el atributo ficha para imprimirlo incluso estando privado
    def gettodo(self):                             #Se define el metodo gettodo
        print("Documento:",app.getdocum())         #Se imprime el metodo getdocum con el objeto app
        print("Nombre:",app.getNombre())            #Se imprime el metodo getNombre con el objeto app
        print("Ficha:",app.getficha())            #Se imprime el metodo getficha con el objeto app
app=aprendiz("luis",464654,38726847628)            #Se define el objeto
print(app.gettodo())                               #Se imprime el metodo gettodo para que llame los metodos de la clase padre desde la herencia aprendiz
