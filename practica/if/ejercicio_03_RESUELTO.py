
"""

Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


"""

idivisor = input("introduce el divisor\n")
idividendo = input("introduce el dividendo\n")

try :
    divisor = float(idivisor)
    dividendo = float(idividendo)

except:
    print("Introduce un numero valido")
    quit()

if divisor == 0:
    print("Introduce un numero valido")
    quit()

resultado = divisor / dividendo

print(resultado)