art={}
def can(spotify):
    can=input("Agregue una canción:")
    art.update({can:{}})
    return spotify
def com(spotify):
    canción=input("Nombre de la canción para su registro:")
    if canción not in spotify:
        print("La canción no esta registrada:")
        print("Agregue una canción primero:")
    artis=input("Ingrese nombre del artista:")
    gene=input("Ingrese genero musical:")
    dur=input("Ingrese la duración de la canción:")
    if canción in spotify:
        spotify.update({canción:{"Artista":artis,"Genero":gene,"Duración":dur}})
def bus1(spotify):
    busca=input("Buscar artista:")
    for x in (spotify.values()):
        if busca==x["Artista"]:
            print("El artista registrado es:",busca)
        else:
            print(busca,"No esta registrado el artista rectifique")
can(art)
com(art)
bus1(art)
print(art)
