dia = int(input("Indica el día > "))
print()
mes = int(input("Indica el mes > "))
print()
año = int(input("Indica el año > "))
print()
print(f"Has indicado {dia}-{mes}-{año}")
if (dia == 31) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    dia = 1
    if mes == 12:
        mes = 1
        año = año+1
    else:
        mes == mes+1
elif (dia == 30) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    dia = 1
    mes == mes+1
elif (dia == 28) and (mes == 2 ) and (año%400==0) or (año%4==0): 
    dia = 29
elif (dia == 29) and (mes == 2 ) and (año%400==0) or (año%4==0):
    dia = 1 
    mes == mes+1
elif (dia == 28) and (mes == 2 ):
    dia = 1 
    mes == mes+1
else:
    dia = dia+1    
print() 
print(f"El dia sigiente será {dia}-{mes}-{año}")