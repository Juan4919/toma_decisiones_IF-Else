letra = input("Indica la letra de calificación > ").upper()

print()

if letra == "A+":
    print("La calificación es 4.0")     
elif letra == "A":
    print("La calificación es 4.0")
elif letra == "A-":
    print("La calificación es 3.7")
elif letra == "B+":
    print("La calificación es 3.3")
elif letra == "B":
    print("La calificación es 3.0")
elif letra == "B-":
    print("La calificación es 2.7")
elif letra == "C+":
    print("La calificación es 2.3")
elif letra == "C":
    print("La calificación es 2.0")
elif letra == "C-":
    print("La calificación es 1.7")
elif letra == "D+":
    print("La calificación es 1.3")
elif letra == "D":
    print("La calificación es 1")
elif letra == "F":
    print("La calificación es 0")
else: 
    print("La letra indicada es incorrecta")