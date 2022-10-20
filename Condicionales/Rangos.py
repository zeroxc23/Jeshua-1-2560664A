a = int(input("Ingrese numero"))
if (a<10)and(a<10000):
    print("Tiene una cifra")
elif(a<100)and(a<10000):
    print("Tiene 2 cifras")
elif (a<1000)and(a<10000):
    print("tiene 3 cifras")
elif (a<10000)and(a<10000):
    print("Tiene 4 cifras")
elif (a>10000):
    print ("Dato erroneo limite excedido")
