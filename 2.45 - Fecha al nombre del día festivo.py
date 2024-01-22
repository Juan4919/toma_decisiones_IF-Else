dia = int(input("Indica el día > "))
mes = input("Indica el mes > ").lower()
print()
if dia == 1 and mes == "enero":
    print("La fecha indicada es año nuevo")
elif dia == 1 and mes == "julio":
    print("La fecha indicada es el día nacional de Canadá")
elif dia == 25 and mes == "diciembre":
    print("La fecha inicada es el día de Navidad")
else:
    print("La fecha indicada no se corresponde a ninguna festividad")
print()