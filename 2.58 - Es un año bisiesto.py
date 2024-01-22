año = int(input("Indica el año que deseas comprobar > "))
print
if año%400==0:
    print("El año es bisiesto")
elif año%100==0:
    print("NO es año bisiesto")
elif año%4==0: 
    print("El año es bisiesto")
else:
    print("NO es año bisiesto")