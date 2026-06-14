print("ESCRIBE UNA CADENA DE TEXTL\n")
primera = input("Primer texto: \n").lower()
print(primera)
segunda = input("Segundo texto: \n").lower()
print(segunda)
for item in primera:
    if item not in segunda :
        print("desbalanceada")
        break
    else: print("")
else: print("balanceada")