#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def codi(a):
    cod=['m','u','r','c','i','e','l','a','g','o'] 
    cod1=["M","U","R","C","I","E","L","A","G","O"]
    print("Referencia:",'murcielago')
    print("Referencia:",'0123456789')
    sad=''
    for i in range(len(a)):
        if a[i] in cod:
            sad+=str(cod.index(a[i]))
        elif a[i] in cod1:
            sad+=str(cod1.index(a[i]))
        else:
            sad+=a[i]
    print(sad)
    print("Palabra escogida:",a) 
x=input('Ingrese palabra a encriptar:')
codi(x)   
