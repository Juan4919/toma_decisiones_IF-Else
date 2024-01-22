valor = float(input("Indica el valor del terremoto > "))
print()

if valor <= 2.0:
    print(f"Un terremoto de magnitud {valor}, es considerado micro")
elif valor >= 2.0 and valor < 3.0:
    print(f"Un terremoto de magnitud {valor}, es considerado muy leve")
elif valor >= 3.0 and valor < 4.0:
    print(f"Un terremoto de magnitud {valor}, es considerado leve")
elif valor >= 4.0 and valor < 5.0:
    print(f"Un terremoto de magnitud {valor}, es considerado muy ligero")
elif valor >= 5.0 and valor < 6.0:
    print(f"Un terremoto de magnitud {valor}, es considerado moderado")
elif valor >= 6.0 and valor < 7.0: 
    print(f"Un terremoto de magnitud {valor}, es considerado fuerte")
elif valor >= 7.0 and valor < 8.0: 
    print(f"Un terremoto de magnitud {valor}, es considerado importante")
elif valor >= 8.0 and valor < 10.0:
    print(f"Un terremoto de magnitud {valor}, es considerado desastroso")
elif valor >= 10: 
    print(f"Un terremoto de magnitud {valor}, es considerado catastrófico")







