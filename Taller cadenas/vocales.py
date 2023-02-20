#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def ind(v):
    cont1=0
    cont2=0
    cont3=0
    cont4=0
    cont5=0
    for i in v.lower():
        if i in "aeiou":
            cont1+=1
        elif ord (i) >= 65 and ord (i) <= 90 or ord(i) >= 97 and ord(i) <= 122: 
            cont3+=1
        elif i in "áéíóú":
            cont2+=1
        elif ord (i)>=48 and ord (i)<=57:
            cont4+=1
        else:
            cont5+=1
    print("Consonantes en total:",cont3)
    print("Vocales en total:",cont1)
    print("Vocales con tilde en total:",cont2)
    print("Numeros en total:",cont4)
    print("Caracteres especiales:",cont5)
x=input("Ingrese una palabra al azar:")
print(ind(x))