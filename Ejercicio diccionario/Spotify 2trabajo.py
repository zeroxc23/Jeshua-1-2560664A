art={}
def can(art):
    can=input("Agregue una canción:")
    art.update({can:{}})
    return art
def com(art):
    canción=input("Nombre de la canción para su registro:")
    if canción not in art:
        print("La canción no esta registrada agregue primero:")
    artis=input("Ingrese nombre del artista:")
    gene=input("Ingrese genero musical:")
    dur=input("Ingrese la duración de la canción (mm) y (ss):")
    if canción in art:
        art.update({canción:{"Artista":artis,"Canción":canción,"Genero":gene,"Duración":dur}})
def bus1(art):
    busca=input("Buscar artista:")
    for x in (art.values()):
        if busca==x["Artista"]:
            print("El artista registrado es:",busca)     
            return None
        print(busca,"No esta registrado el artista rectifique:")
def bus2(art):
    busca=input("Buscar canción:")
    for x in (art.values()):
        if busca==x["Canción"]:
            print("La canción registrada es:",busca)
        else:
            print(busca,"No esta registrada la canción rectifique:")
def elim1(art): 
    buscar=input('¿Que artista quiere eliminar?: ') 
    for x in sorted(art.keys()): 
        if buscar==x: 
            del art[x] 
            print("El artista",buscar,"fue eliminada de la lista")
        else:
            print("El artista no esta registrado, no se puede eliminar") 

while True:
    print("1-Ingresar Canción")
    print("2-Completar información entorno a la canción")
    print("3-Buscar artista:")
    print("4-Buscar cancion:")
    print("5-Eliminar artista:")
    print("6-Cancion mas larga:")
    print("7-cancion mas corta:")
    print("8-Todos los datos:")
    zxc=int(input("ingrese el numero correspondiente a la acción que solicite: "))
    match zxc:
        case 1:
            print(can(art))
        case 2:
            print(com(art))
        case 3:
            print(bus1(art))
        case 4:
            print(bus2(art))
        case 5:
            print(elim1(art))
        case 6:
            print(may(art))
        case 7:
            print(men(art))
        case 8:
            print("Lista de canciones: ",art)
        case _:
            print("Opción inexistente")
            break