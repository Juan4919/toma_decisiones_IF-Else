blanco = ['a8', 'a6', 'a4', 'a2', 'b7', 'b5', 'b3', 'b1', 'c8', 'c6', 'c4', 
'c2', 'd7', 'd5', 'd3', 'd1', 'e8', 'e6', 'e4', 'e2', 'f7', 'f5', 'f3', 'f1', 
'g8', 'g6', 'g4', 'g2', 'h7', 'h5', 'h3', 'h1']
negro = ['b8', 'b6', 'b4', 'b2', 'a7', 'a5', 'a3', 'a1', 'd8', 'd6', 'd4', 
'd2', 'c7', 'c5', 'c3', 'c1', 'f8', 'f6', 'f4', 'f2', 'e7', 'e5', 'e3', 'e1', 
'h8', 'h6', 'h4', 'h2', 'g7', 'g5', 'g3', 'g1']
print()
posicion = input("Ingresa una posición válida (por ejemplo b3) > ")
print()
if posicion in blanco:
    print("El color es blanco.")
elif posicion in negro:
    print("El color es negro.")   
else: 
    print("La posición indicada no es válida.")
