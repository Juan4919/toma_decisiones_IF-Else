valor = float(input("Indica el valor > "))
print()
if valor == 0.0:
    print("Tu rendimiento es inaceptable, por lo que no recibirás ninguna gratificación")
elif valor == 0.4:
    print("Tu rendimiento es aceptable, por lo que recibirás ",(2400*0.4),"€ de gratificación")
elif valor == 0.6:
    print("¡Tienes un desempeño meritorio!, por lo que recibirás",(2400*0.6),"€ de gratificación")
print()
