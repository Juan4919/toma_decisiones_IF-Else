matricula = input("Indica la matricula (3 mayusculas + 3 dígitos o 4 dígitos + 3 mayúsculas) > ")
print()
if len(matricula) == 6:
    matricula_numeros = int(matricula[3:])
    matricula_letras = str(matricula[:3]).upper()
    print(f"La matrícula{matricula_letras+matricula_numeros} es un modelo antiguo")
elif len(matricula) == 7:
    matricula_numeros = int(matricula[:4])
    matricula_letras = str(matricula[4:]).upper()
    print(f"La matrícula{matricula_numeros,matricula_letras} es un modelo de los nuevos")
else:
    print("La matrícula indicada es incorrecta o no existe")
    

   
    
