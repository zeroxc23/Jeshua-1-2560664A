#Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula 
def tip(z):
    if (z[-1]==chr(225)or z[-1]==chr(233) or z[-1]==chr(237) or z[-1]==chr(243) or z[-1]==chr(250) or z[-1] in 'ns'):
        print("Es aguda")
    elif (z[-1]not in chr(225)or z[-1] not in chr(233) or z[-1] not in chr(237) or z[-1] not in chr(243) or z[-1] not in chr(250) and z[-1] not in ('ns') ):
        print("Es grave")
m=input("Ingrese una palabra al azar contando tildes:")
tip(m)
