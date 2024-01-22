edad = float(input("Introduce la edad del perro> "))

if edad <= 2:
    print("El perro tiene 21 años")
elif edad >= 2.1: 
    edad_final = ((edad - 2)*4)+21
    print(f"El perro tiene {int(edad_final)} años")