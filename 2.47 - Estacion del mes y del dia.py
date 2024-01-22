primavera = ['marzo', 'abril', 'mayo', 'junio']
verano = ['junio', 'agosto', 'septiembre']
otoño = ['septiembre', 'octubre', 'noviembre', 'diciembre']
invierno = ['diciembre', 'enero', 'febrero', 'marzo']

mes = input("Ingresa el mes > ")
dia = int(input("Ingresa el día > "))

if mes == "enero" or mes == "febrero":
    temporada = "invierno"
elif mes == "marzo":
    if dia < 20: 
        temporada = "invierno"
    else:
        temporada = "primavera"
if mes == "abril": 
    if mes >= 20:
        temporada = "primavera"
elif mes == "mayo":
    temporada = "primavera"
elif mes == "junio":
    if dia < 21:
        temporada = "primavera"
    else: 
        temporada = "verano"
if mes == "julio" or mes == "agosto":
    temporada = "verano"
elif mes == "septiembre":
    if dia < 22:
        temporada = "verano"
    else:
        temporada = "otoño"
if mes == "octubre" or mes == "noviembre":
    temporada = "otoño"
elif mes == "diciembre":
    if dia < 21:
        temporada = "otoño"
    else:
        temporada = "invierno"
