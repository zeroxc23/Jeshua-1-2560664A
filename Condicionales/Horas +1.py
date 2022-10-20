A = int(input("Ingrese horas"))
B = int(input("Ingrese minutos"))
C = int(input("Ingrese segundos"))
if (C>58):
    C=00
    B = B+1
if(B>58):
    B==00
    A = A+1 
    B=B>58
    B=00   
if(A>23):
    A=00
    A=A>23
    A=00

print("HH:",A,"MM:",B,"SS:",C)


