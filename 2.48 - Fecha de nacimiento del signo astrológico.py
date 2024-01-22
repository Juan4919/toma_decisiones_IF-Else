dia = int(input("Indica el día en que naciste > "))
mes = input("Indica tu mes de nacimiento > ")

dia = int(input("Indica el día en que naciste > "))
mes = input("Indica tu mes de nacimiento > ")

if (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19):
    print("Tu signo del zodíaco es Capricornio")
elif (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18):
    print("Tu signo del zodíaco es Acuario")
elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20):
    print("Tu signo del zodíaco es Piscis")
elif (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
    print("Tu signo del zodíaco es Aries")
elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
    print("Tu signo del zodíaco es Tauro")
elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20):
    print("Tu signo del zodíaco es Géminis")
elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22):
    print("Tu signo del zodíaco es Cáncer")
elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
    print("Tu signo del zodíaco es Leo")
elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22):
    print("Tu signo del zodíaco es Virgo")
elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22):
    print("Tu signo del zodíaco es Libra")
elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21):
    print("Tu signo del zodíaco es Escorpio")
elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21):
    print("Tu signo del zodíaco es Sagitario")
else:
    print("Mes o día no válido.")
