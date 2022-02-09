"""
          Ejercicio 4

Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


"""

longitud = 16

input_numero = input("Escribe el numero telefonico con el codigo y la extension: ")

if len(input_numero) is not longitud :
    print("introduce un numero valido")
    quit()


print(input_numero[4:13])