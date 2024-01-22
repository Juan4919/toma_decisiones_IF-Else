valor = float(input("Indica el valor de calificación > "))
print()

if valor > 4.0:
    print("La calificación es A+")     
elif valor == 4:
    print("La calificación es A")
elif valor >= 3.7:
    print("La calificación es A-")
elif valor >= 3.3:
    print("La calificación es B+")
elif valor >= 3.0:
    print("La calificación es B")
elif valor >= 2.7:
    print("La calificación es B-")
elif valor >= 2.3:
    print("La calificación es C+")
elif valor >= 2.0:
    print("La calificación es C")
elif valor >= 1.7:
    print("La calificación es C-")
elif valor >= 1.3:
    print("La calificación es D+")
elif valor >= 1.0:
    print("La calificación es D")
elif valor >= 0:
    print("La calificación es F")
else: 
    print("El valor indicad0 es incorrecta")