#lista
print("Escriba una lista de numeros y se sumarán las entradas que no estén repetidas, escriba 'salir' para cerrar la lista")
lista = []
suma = 0
while True :
    entrada = input()
    if entrada == "salir":
        break
    else:
        entero_entrada = int(entrada)
        lista.append(entero_entrada)
print(lista)

for item in lista:
    
    if lista.count(item) >= 2:
        print("REPETIDO")
    else:
        suma = suma + item
print("Suma total sin repetidos: \n")
print(suma)
   