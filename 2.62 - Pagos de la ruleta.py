import random

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
verdes = [0, 00]

juega = input("Para jugar pulsa enter > ")
numero = random.choice(rojos) or random.choice(negros) or random.choice(verdes)
print()
print(f"¡El giro terminó en {numero}!")
print()
print(f"Paga {numero}")
if numero in rojos: 
    print("Paga rojo")
elif numero in negros:
    print("Paga negro")
if numero%2==0:
    print("Paga par")
elif numero%2==1:
    print("Paga impar")
if numero >= 1 and numero <= 18: 
    print( "Paga 1 a 18")
elif numero >= 19 and numero <= 36:
    print("Paga 19 a 36")
if numero == 0 or numero == 00:
    print(f"Pagar {numero}")
print()