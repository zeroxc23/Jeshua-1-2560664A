class usuario:
    def __init__(self,nombre,direccion,telefono,n,n1):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__n=n
        self.__n1=n1            
    def getnom(self):
        return self.__nombre
    def getd(self):
        return self.__direccion
    def getnum(self):
        return self.__telefono
    def get(self):
        return self.__n
    def get1(self):
        return self.__n1
    def sab(self,n):
        if "#"in n:
            print("-----------")
            print("Estudiante")
            print("-----------")
        elif "@"in n:
            print("-----------")
            print("Docente")
            print("-----------")
        else:
            print("-----------")
            print("Usuario no encontrado")
    def lib(self,n1):
        if n1==1:
            print("Solcita reserva de:")
            print("Libro")
            print("-----------")
        elif n1==2:
            print("Solcita reserva de:")
            print("Revista")
            print("-----------")
        else:
            print("-----------")
            print("Producto no encontrado")
            print("-----------")
#//////////////////////////////////////////////////////////////////////////////////////
class libro:
    def __init__(self,titulo,tipo,autor,editorial):
        self.__titulo=titulo
        self.__tipo=tipo
        self.__editorial=editorial
        self.__autor=autor
    def gett(self):
        return self.__titulo
    def gettipo(self):
        return self.__tipo
    def getautor(self):
        return self.__autor
    def geteditorial(self):
        return self.__editorial
class revista:
    def __init__(self,titulo,tipo,autor,editorial):
        self.__titulo=titulo
        self.__tipo=tipo
        self.__editorial=editorial
        self.__autor=autor
    def gett(self):
        return self.__titulo
    def gettipo(self):
        return self.__tipo
    def getautor(self):
        return self.__autor
    def geteditorial(self):
        return self.__editorial   
#//////////////////////////////////////////////////////////////////////////////////////
class pedido(usuario):
    def __init__(self, nombre, direccion, telefono, n, n1,  id, titulo, codigo):
        self.__id=id
        self.__titulo=titulo
        self.__codigo=codigo
        usuario .__init__(self, nombre, direccion, telefono, n, n1)
    def getid(self):
        return self.__id
    def gettitulo(self):
        return self.__titulo
    def getcodigo(self):
        return self.__codigo
    def datos(self):
        print("-----------")
        print("Datos del usuario")
        print("Nombre:",a.getnom())
        print("Dirección:",a.getd())
        print("Telefono:",a.getnum())
        print("Id:", a.getid())
        print("Titulo:",a.gettitulo())
        print("Codigo:", a.getcodigo())
        a.sab(n)
        a.lib(n1)


n=input("Ingrese # si es un estudiante//Ingrese @ si es un docente:")
n1=int(input("Ingrese 1 para solicitar un libro//Ingrese 2 para solicitar una revista:"))
a= pedido("Luis","Kr-15",3267276,n,n1,156264512,"Scorpio city",53523)
a.datos()
