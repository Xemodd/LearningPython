print(" ESTACIONAMIENTO \nSi tu vehículo tiene más de 5h\nobtienes un 10% de descuento")
vehiculo = ""
precio = 0
horas = 0
while True:
    vehiculo = input("Ingrese su vehículo:\nMoto\nAuto\nBici\n")
    if vehiculo.lower() == "auto":
        precio = precio + 25
        break
    elif vehiculo.lower() == "moto":
        precio = precio + 15
        break
    elif vehiculo.lower() == "bici":
        precio = precio + 5
        break
    else:
        print("Vehiculo no admitido\n")


while True:
    horas = input("Ingrese la cantidad de horas:\n")
    horasparse = ""
    try: horasparse =int(horas)
    except ValueError:
        print("valor invalido, intente de nuevo")
        continue
    if horasparse < 1:
             print("Valor no admitido")
    elif horasparse <= 5:
             total= precio*horasparse
             print("Tu total es: ",total)
             break
    elif horasparse >= 6:
             horas_extra = horasparse - 5
             horas_normales = precio*5
             hora1 = (horas_extra* precio) - (horas_extra* precio*0.1)
             total = horas_normales + hora1
             print("Obtienes un 10% de descuento en el\nestacionamiento de tu ",vehiculo,"\nTotal a pagar: ",total)
             break
          