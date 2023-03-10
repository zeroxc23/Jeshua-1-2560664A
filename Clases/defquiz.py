class lector:
    def __init__(self,nombre,direccion,telefono,ID):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__ID=ID
        self.__lista=[]
    def agregar(self,usuario):
        self.__lista.append(usuario)
    def verusuarios(self):
        return self.__lista
    def getID(self):
        return self.__ID
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    def gettodo(self):
        print("-----------------")
        print("Datos de usuario")
        print("Nombre:", a.getnombre())
        print("Dirección:", a.getdireccion())
        print("Telefono:", a.gettelefono())
        print("Id del bibliotecario: responsable",a.getID())
class pedido:
    def __init__(self,id,titulo,codigo,usuario):
        self.__id=id
        self.__titulo=titulo
        self.__codigo=codigo
        self.__usuario=usuario
    def getusuario(self):
        if self.__usuario=="1":
            print("Ingreso con la cuenta estudiante")
        elif self.__usuario=="2":
            print("Ingreso con la cuenta docente")
        else:
            print("Usuario no encontrado")
    def getid(self):
        return self.__id
    def getcodigo(self):
        return self.__codigo
    def gettitulo(self):
        return self.__titulo
    def gettodox(self):
        print("-----------------")
        print("Datos del pedido")
        print("Id:",usu.getid())
        print("Codigo:",usu.getcodigo())
        print("Titulo:",usu.gettitulo())
class libro:
    def __init__(self,titulo,tipo,autor,editorial):
        self.__titulo=titulo
        self.__tipo=tipo
        self.__autor=autor
        self.__editorial=editorial
    def gettitulo(self):
        return self.__titulo
    def gettipo(self):
        return self.__tipo
    def getautor(self):
        return self.__autor
    def geteditorial(self):
        return self.__editorial
class revista:
    def __init__(self,titulo1,tipo1,autor1,editorial1):
        self.__titulo1=titulo1
        self.__tipo1=tipo1
        self.__autor1=autor1
        self.__editorial1=editorial1
    def gettitulo1(self):
        return self.__titulo1
    def gettipo1(self):
        return self.__tipo1
    def getautor1(self):
        return self.__autor1
    def geteditorial1(self):
        return self.__editorial1
class entrega(libro,revista):
    def __init__(self,titulo,tipo,autor,editorial,titulo1,tipo1,autor1,editorial1,nota1):
        self.__nota1=nota1
        super().__init__(titulo,tipo,autor,editorial)
        revista.__init__(self,titulo1,tipo1,autor1,editorial1)
    def getnota(self):
        return self.__nota1
    def getlib(self,nota1):
        if nota1=="l":
            print("-----------------")
            print("Datos libro")
            print("Titulo:",a1.gettitulo())
            print("Tipo:",a1.gettipo())
            print("Autor:",a1.getautor())
            print("Editorial:",a1.geteditorial())
        elif nota1=="r":
            print("-----------------")
            print("Datos revista")
            print("Titulo:",a1.gettitulo1())
            print("Tipo:",a1.gettipo1())
            print("Autor:",a1.getautor1())
            print("Editorial:",a1.geteditorial1())
class reserva:
    def __init__(self,fechai,fechafin,fechai1,fechafin1,dato):
        self.__fechai=fechai
        self.__fechafin=fechafin
        self.__fechai1=fechai1
        self.__fechafin1=fechafin1
        self.__dato=dato
    def getdato4(self):
        return self.__dato
    def getfechai(self):
        return self.__fechai
    def getfechaf(self):
        return self.__fechafin
    def getfechai1(self):
        return self.__fechai1
    def getfechaf1(self):
        return self.__fechafin1
    def getdatof(self,dato):
        if dato=="3":
            print("-----------------")
            print("Fechas libro")
            print("Fecha inicio:",l.getfechai())
            print("Fecha fin:",l.getfechaf())
        elif dato=="4":
            print("-----------------")
            print("Fechas revista")
            print("Fecha inicio:",l.getfechai1())
            print("Fecha fin:",l.getfechaf1())

while True:
    print("-----------------")
    print("1-Inicar sesión")
    print("2-Completar información entorno a tipo de cuenta")
    print("3-Datos del material que solicita reservar:")
    print("4-Datos del pedido:")
    print("5-Consultar reservas:")
    print("6-Cerrar sistema")
    zxc=int(input("ingrese el numero correspondiente a la acción que solicite: "))
    match zxc:
        case 1:
            print("-----------------")
            x=input("Ingrese nombre de usuario:")
            x1=input("Ingrese dirección:")
            x2=input("Ingrese numero telefonico:")
            a=lector(x,x1,x2,6576)
            a.gettodo()
        case 2:
            print("-----------------")
            n=input("Ingrese 1 si es estudiante//Ingrese 2 si es docente:")
            usu=pedido(2324,"Solicitud de reserva",8383,n)
            a.agregar(usu)
            for c in a.verusuarios():
               print(c.getusuario())
               break
        case 3:
            print("-----------------")
            print("Datos del libro y revista disponible")
            c1=input("Ingrese l para saber los datos del libro//Ingrese r para saber los datos de la revista:")
            a1=entrega("Scorpio city","Suspenso","Mario mendoza","La casa","La nueva moda","rating","Franchesca","AVON",c1)
            a1.getlib(c1)
        case 4:
            print("-----------------")
            usu=pedido(2324,"Solicitud de reserva",8383,n)
            usu.gettodox()
        case 5:
            print("-----------------")
            f=input("Ingrese 3 para consultar fechas de disponibilidad del libro//Ingrese 4 para consultar fechas de disponibilidad de la revista:")
            l=reserva("9/03/2023","12/04/2023","5/04/2023","14/06/2023",f)
            l.getdatof(f)
        case 6:
            print("-----------------")
            print("Abandono el sistema")
            break