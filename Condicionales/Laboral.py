h1 = int(input("Horas de trabajo"))
h2 = float(h1)
h3 = h1-40
h4 = (40*2600)+(h3*5000)
h5 = (h2*2600)
if h2>40:
    print("salario total es:",h4)
elif h2<40:
    print("salario total:",h5)