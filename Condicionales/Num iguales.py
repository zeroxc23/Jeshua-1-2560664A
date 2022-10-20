n1 =int(input("ingrese primer numero: "))
n2 =int(input("ingrese segundo numero: "))
n3 =int(input("ingrese tercer numero: "))
p1 = (n1==n2==n3)
p2 = (n1==n2!=n3)or(n1!=n2==n3)or(n2!=n3==n1)
p3 = (n1!=n2!=n3!=n2!=n1)
if p1:
    print("Todos iguales")
elif p2:
    print("Dos iguales")
elif p3:
    print("Todos distintos")



