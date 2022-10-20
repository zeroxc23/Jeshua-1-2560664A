
from math import sqrt


def resolver_ecuacion(a, b ,c ):
    determinante=b**2-4*a*c


    if determinante >0:
        x_1=-b + sqrt(b**2-4*a*c) / (2*a)
        x_2=-b - sqrt(b**2-4*a*c) / (2*a)
        return x_1, x_2

    elif determinante  == 0:
        x_1 = -b /(2*a)
        return(x_1,)

    else:
        return tuple()    

print(resolver_ecuacion(34,75,23))        