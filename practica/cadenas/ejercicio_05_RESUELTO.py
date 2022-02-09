"""

        Ejercicio 5


Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

"""


frase = input("Escribe una frase y te la devuelvo volteada: ")

frase_volt = "" .join(reversed(frase))

print(frase_volt)