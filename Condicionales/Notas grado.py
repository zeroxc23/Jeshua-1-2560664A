# 5 valores representadas en notas 
a = input("Ingrese una nota")
b = float(a)
if b >11:
    print("valor invalido")
elif b<= 1:
    print("reprobado")
elif b<=3:
    print("insuficiente")
elif b<=5:
    print("suficiente")
elif b<=7:
    print("bien")
elif b<=10:
    print("excelente")