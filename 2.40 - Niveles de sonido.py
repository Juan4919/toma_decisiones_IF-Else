decibelios = float(input("Indica los decibelios de sonido > "))
if decibelios > 130:
    print("El valor supera los 130db de un martillo neumático")
elif decibelios == 130: 
    print("El valor iguala al sonido de un martillo neumático")
elif decibelios < 130 and decibelios > 106:
    print("El valor está entre 106db de un cortacésped a gasolina y 130db de un martillo neumático")
elif decibelios == 106: 
    print("El valor iguala al sonido de un cortacésped a gasolina")
elif decibelios < 106 and decibelios > 70:
    print("El valor está entre 70db de un despertador y 106db de un cortacésped a gasolina")
elif decibelios == 70: 
    print("El valor iguala al sonido de un despertador")
elif decibelios < 70 and decibelios > 40:
    print("El valor está entre 40db de un cuarto tranquilo y 70db de un despertador")
elif decibelios == 40: 
    print("El valor iguala al sonido de un cuarto tranquilo")
elif decibelios < 40: 
    print("El valor es por debajo de los 40db de un cuarto tranquilo")