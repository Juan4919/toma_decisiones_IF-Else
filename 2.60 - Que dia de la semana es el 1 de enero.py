año = int(input("Indica el año que quieres comprobar > "))
dia_semana = (año + año - 1 // 4 - año - 1 // 100 + año - 1 // 400) % 7 +1
if dia_semana == 0:
    dia_semana = "domingo"
if dia_semana == 1:
    dia_semana = "lunes"
if dia_semana == 2:
    dia_semana = "martes"
if dia_semana == 3:
    dia_semana = "miércoles"
if dia_semana == 4:
    dia_semana = "jueves"
if dia_semana == 5:
    dia_semana = "viernes"
if dia_semana == 6:
    dia_semana = "sábado"

print("El día de la semana para el 1 de enero de", año, "es:", dia_semana)
