lista=[]
print("Ingrese una lista de numeros \nSe hará una sumatoria del valor \nmas alto y el más bajo \nEscriba 's' para cerrar la lista \nLa lista debe tener minimo 2 numeros \n")
while True:
    entrada = input()
    if entrada == "s" and len(lista) > 1:
        break
    else:
        try:
            entero_entrada = int(entrada)
            lista.append(entero_entrada)
        except ValueError:
            print("Respuesta Inválida")
        
print(lista)

menor = min(lista)
mayor = max(lista)
suma = menor + mayor
print("la suma del menor y mayor valor es: \n", suma)