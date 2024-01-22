'''
Notas:
-C4
-D4
-E4
-F4
-G4
-A4
-B4
'''

nota = input("Indica la nota que quieres conocer > ").upper()
print()
if nota == 'C4':
    print("La nota indicada tiene una frecuencia de 261,63Hz")
elif nota == 'D4':
    print("La nota indicada tiene una frecuencia de 293,66Hz")
elif nota == 'E4':
    print("La nota indicada tiene una frecuencia de 329,63Hz")
elif nota == 'F4':
    print("La nota indicada tiene una frecuencia de 349,23Hz")
elif nota == 'G4':
    print("La nota indicada tiene una frecuencia de 392,00Hz")
elif nota == 'A4':
    print("La nota indicada tiene una frecuencia de 440,00Hz")
elif nota == 'B4':
    print("La nota indicada tiene una frecuencia de 493,88Hz")
elif len(nota) == 2:
    numero = int(nota[1])  # Convierte la segunda letra a un número entero
    if numero < 4:
        valor = 261.63 / (2 ** (4 - numero))  # Corregir la coma y usar el operador de doble asterisco
        print(valor)
    elif numero > 4: 
        valor = 261.63 * (2 ** (numero - 4))
        print(valor)
    else:
        print("Número no reconocido en la segunda posición.")
