lado1 = float(input("Indica la medida del primer lado del triángulo > "))
lado2 = float(input("Indica la medida del segundo lado del triángulo > "))
lado3 = float(input("Indica la medida del tercer lado del triángulo > "))
print()
if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3:
    print("El triángulo es isósceles")
elif lado2 == lado1 or lado2 == lado3:
    print("El triángulo es isósceles")
elif lado3 == lado2 or lado3 == lado1:
    print("El triángulo es isósceles")
elif lado1 != lado2 and lado2 != lado3:
    print("El triángulo es escaleno")