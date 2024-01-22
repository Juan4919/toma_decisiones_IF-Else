valor = int(input("Introduce el valor del billete que quieres conocer > "))
print()
if valor == 1: 
    print("El billete que indicas, lleva la cara de George Washington")
elif valor == 2: 
    print("El billete que indicas, lleva la cara de Thomas Jefferson")
elif valor == 5: 
    print("El billete que indicas, lleva la cara de Abraham Lincoln")
elif valor == 10: 
    print("El billete que indicas, lleva la cara de Alexander Hamilton")
elif valor == 20: 
    print("El billete que indicas, lleva la cara de Andrew Jackson")
elif valor == 50: 
    print("El billete que indicas, lleva la cara de Ulysses S. Grant")
elif valor == 100: 
    print("El billete que indicas, lleva la cara de Benjamín Franklin")
else:
    print("No existe ningún billete con el valor que indicas")
print()