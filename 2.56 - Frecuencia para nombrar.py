radiacion = float(input("Indica el valor de radiación a comprobar > "))
print
if radiacion < (3*109):
    print("El valor pertenece a ondas de radio")
elif (radiacion >= 3*109) and (radiacion < 3*1012):
    print("El valor pertenece a ondas microondas")
elif (radiacion >= 3*1012) and (radiacion < 4.3*1014):
    print("El valor pertenece a ondas infrarojas")
elif (radiacion >= 4.3*1014) and (radiacion < 7.5*1014):
    print("El valor pertenece a ondas de luz visible")
elif (radiacion >= 7.5*1014) and (radiacion < 3*1017):
    print("El valor pertenece a ondas de luz ultravioleta")
elif (radiacion >= 7.5*1017) and (radiacion < 3*1019):
    print("El valor pertenece a ondas de rayos X")
elif (radiacion >= 3*1019):
    print("El valor pertenece a ondas de rayos gamma")
else: 
    print("El valor introducido es incorrecto")