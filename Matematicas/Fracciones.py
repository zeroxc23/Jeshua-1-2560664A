n1 = int(input("ingrese un numerador 1"))
d1 = int(input("ingrese un denominador 1"))
n2 = int(input("ingrese un numerador 2"))
d2 = int(input("ingrese un denominador 2"))
# Solución homogenea
if (d1==d2):

    print  ("Resultado homogeneo")
    suma1 = (n1 + n2)/d1

    resta1 = (n1-n2)
    dresta = ( resta1/d1 )

    multi1 = (n1*n2)
    multi1_0 = (d1*d2)
    totalmulti = (multi1/multi1_0) 

    divi1 = (n1*d2)
    divi1_0 = (d1*n2)
    totaldivi = (divi1/divi1_0)

    print ("resultado suma es:", suma1)
    print ("resultado rsta es:",dresta)
    print ("resultado multiplicación es:", totalmulti)
    print ("resultado divisón es:", totaldivi)

# Solución heterogenea
else:

    print("Resultado heterogeneo")

    suma2 = (n1*d2)
    suma2_0= (d1*n2)
    ressuma = (suma2 + suma2_0)
    suma22 = (d1*d2)
    totalsuma2 = (ressuma/suma22)

    resta2 = (n1*d2)
    resta2_0 = (d1*n2)
    resresta = (resta2-resta2_0)
    resta22 = (d1*d2)
    totalresta2 = (resresta/resta22)

    multi2 = (n1*n2)
    multi2_0 = (d1*d2)
    totalmulti2 = (multi2/multi2_0)

    divi2 = (n1*d2)
    divi2_0 = (d1*n2)
    resdivi = (divi2/divi2_0)

    print ("Resultado suma:",totalsuma2)
    print ("Resultado resta:",totalresta2)
    print ("Resultado multiplicación:",totalmulti2)
    print ("Resultado división:",resdivi)
  




