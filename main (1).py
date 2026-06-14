print("FIZZ BUZZ WHIZ EN PYTHON")
i=0
rango = input("Escribe el rango en el que se correrá el programa")
int_rango = int(rango)
for i in range ( 0, int_rango + 1):
    i + 1
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 7 == 0:
        print("whiz")
    elif i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("fizz buzz whiz")
    else: print (i)
    