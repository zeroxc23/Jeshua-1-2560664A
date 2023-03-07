class usuario:
    def __init__(self,nombre,direccion,telefono,n,n1,n2):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__n=n
        self.__n1=n1 
        self.__n2=n2           
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
    def get2(self):
        return self.__n2
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
    def sino(slef,n2):
        if n2==3:
            print("Material entregado en la fecha correspondiente")
        elif n2==4:
            print("Material no entregado en la fecha correspondiente")
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
    def getod(self):
        print("-----------")
        print("Datos del libro")
        print("Titulo:",w.gett())
        print("Tipo:",w.gettipo())
        print("Autor:",w.getautor())
        print("Editorial:",w.geteditorial())
    
class revista:
    def __init__(self,titulo1,tipo1,autor1,editorial1):
        self.__titulo1=titulo1
        self.__tipo1=tipo1
        self.__editorial1=editorial1
        self.__autor1=autor1
    def gett(self):
        return self.__titulo1
    def gettipo(self):
        return self.__tipo1
    def getautor(self):
        return self.__autor1
    def geteditorial(self):
        return self.__editorial1
    def gettod1(self):
        print("-----------")
        print("Datos revista:")
        print("Titulo:",x.gett())
        print("Tipo:",x.gettipo())
        print("Autor:",x.getautor())
        print("Editorial:",x.geteditorial())

#//////////////////////////////////////////////////////////////////////////////////////
class pedido(usuario):
    def __init__(self, nombre, direccion, telefono, n, n1,n2,id, titulo, codigo):
        self.__id=id
        self.__titulo=titulo
        self.__codigo=codigo
        usuario .__init__(self, nombre, direccion, telefono, n, n1,n2)
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
        a.sino(n2)


n=input("Ingrese # si es un estudiante//Ingrese @ si es un docente:")
n1=int(input("Ingrese 1 para solicitar un libro//Ingrese 2 para solicitar una revista:"))
n2=int(input("Ingrese 3 para saber si se ha entregrado//Ingrese 4 para saber si no se ha entregado:"))
a= pedido("Luis","Kr-15",3267276,n,n1,n2,156264512,"Scorpio city",53523)
#x=materia("Scorpiocity","terror","Mario mendoza",)
a.datos()
w=libro("Scorpio city","terror","Mario","Chupachota")
x=revista("Maquillaje bintachg","Popular","Franchesca","Avon")
x.gettod1()
w.getod()
