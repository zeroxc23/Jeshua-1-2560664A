class usuario:
    def __init__(self,nombre,direccion,telefono,cuenta):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__cuenta=cuenta
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    def getcuenta(self):
        return self.__cuenta
    def getcont(self):
        if self.__cuenta=="#":
            print("Ingreso con usuario de estudiante")
        elif self.__cuenta=="@":
            print("Ingreso con usuario de docente")
        else:
            print("tipo de usuario no encontrado")

class material:
    def __init__(self,dato):
        self.__dato=dato
    def getdat(self):
        if self.__dato=="1":
            print("Datos del libro:")
            print("Titulo: Scorpìo city")
            print("Tipo: Suspenso")
            print("Autor: Mario mendoza")
            print("Editorial: La casa del libro")
        elif self.__dato=="2":
            print("Datos de la revista:")
            print("Titulo: Lo mas popular")
            print("Tipo: Moda")
            print("Autor: Franchesca")
            print("Editorial: Vintage")
        else:
            print("Material no encontrado")
#///////////////////////////////////////////////////////////////////////////////
class pedido(material):
    def __init__(self,dato,id,titulo,codigo):
        self.__id=id
        self.__titulo=titulo
        self.__codigo=codigo
        material .__init__(self,dato)
    def getid(self):
        return self.__id
    def gettitulo(self):
        return self.__titulo
    def getcodigo(self):
        return self.__codigo
    def getpedido(self):
        print("Datos del pedido:")
        print("Id:",z.getid())
        print("Titulo:",z.gettitulo())
        print("Codigo",z.getcodigo())
        print("----------------------")
        print("Datos del material:")
        print(z.getdat())
class bibliotecario(usuario):
    def __init__(self,nombre,direccion,telefono,cuenta,idb):
        self.__idb=idb
        usuario .__init__(self,nombre,direccion,telefono,cuenta)
    def getbibli(self):
        return self.__idb
    def getd(self):
        print("---------------------")
        print("Datos de usuario")
        print("Nombre:",a.getnombre())
        print("Dirección:",a.getdireccion())
        print("Telefono:",a.gettelefono())
        print(a.getcont())
        print("---------------------")
        print("Datos del biliotecario")
        print("ID:",a.getbibli())
        print("---------------------")
c=input("Ingrese # si es estudiante//Ingrese @ si es docente:")
a=bibliotecario("Luis","Kr-15",213828,c,6362363)
a.getd()
x=input("Ingrese 1 para los datos del libro//Ingrese 2 para los datos de la revista:")
z=pedido(x,112312,"Scorpio city",62363)
z.getpedido()