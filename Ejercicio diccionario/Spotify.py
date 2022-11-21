art={"Artist1":{"Artista1":"Elvis Presley","Canción1":"In the guetto","Genero1":"Rock","Duración1":"2:45"},
"Artist2":{"Artista2":"Fredy Mercury","Canción2":"Bohemian Rapsody","Genero2":"Rock","Duración2":"5:55"},
"Artist3":{"Artista3":"Michael Jackson","Canción3":"Beat it","Genero3":"Disco","Duración3":"4:18"}}
print("Artistas codigo de referencias: Artista 1, 2 o 3/Canción 1, 2 o 3/Genero 1, 2 o 3 y Duración 1, 2 o 3")
print("Ejemplo gramatica Artista1")
def bus():
    for i in art:
        a1=input("Busque al artista:")
        if a1 in art[i]:
            print(art[i])
            
    for x in art.values():
        return x
bus()

   