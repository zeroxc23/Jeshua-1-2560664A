#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def codi(a):
    cod=['m','u','r','c','i','e','l','a','g','o']
    print('murcielago')
    print('0123456789')
    sad=''
    for i in range(len(a)):
        if a[i] in cod:
            sad+=str(cod.index(a[i]))
        else:
            sad+=a[i]
    print(sad)            
x=input('ingrese palabra a encriptar:')
codi(x)   