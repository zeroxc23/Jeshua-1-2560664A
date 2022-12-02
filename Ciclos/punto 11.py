a,q=1,0
num1=float(input("ingrese el dividendo"))
num2=float(input("ingrese el divisor"))
if(num1>=num2):
    while ((num1-num2)>=q):
        q=num2*a
        a=a+1
    print("el cociente es"+str(a-1)+"y el residuo es "+str((num1-q)),end=(""))
else:
    print("debe ser menor el dividendo")

