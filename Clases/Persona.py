class persona:
    def __init__(self,nombre):
        self.__nombre=nombre
        #print("constructor")
    def getnom(self):
        return self.__nombre 
    def setn(self,nombre):
        self.__nombre=nombre
obj=persona("Jose")
obj.setn("juan")
print(obj.getnom())
