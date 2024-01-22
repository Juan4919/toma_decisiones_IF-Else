letra = input("Indica la letra que quieres comprobar > ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("La letra indicada es una vocal")
elif letra == 'y':
    print("La letra Y, a veces es vocal y otras veces es consonante")
else: 
    print("La letra indicada es una consonante")