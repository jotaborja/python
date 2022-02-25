"""
    Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

"""

inum = input("por favor introduce un numero: ")
num = int(inum)

for i in range(num, -1, -1):
    print(i, end=", ")