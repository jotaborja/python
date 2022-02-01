"""

    Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


"""

nombre = input("Cual es tu nombre? ")
numero = input("Introduce un numero ")

try:
    numero_convertido = float(numero)
except:
    print("introduce un numero valido")
    quit()

while numero_convertido > 0:
    numero_convertido = numero_convertido - 1
    print(nombre)
