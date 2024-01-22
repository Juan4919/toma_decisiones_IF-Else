onda = float(input("Indica el valor de onda que quieres comprobar > "))
print()
if onda >= 380 and onda <450: 
    print("El espectro es violeta")
elif onda >= 450 and onda < 495: 
    print("El espectro es azul")
elif onda >= 495 and onda < 570: 
    print("El espectro es verde")
elif onda >= 570 and onda < 590: 
    print("El espectro es amarillo")
elif onda >= 590 and onda < 620: 
    print("El espectro es naranja")
elif onda >= 620 and onda < 750: 
    print("El espectro es rojo")
else: 
    print("El valor indicad está fuera del expectro")
print()