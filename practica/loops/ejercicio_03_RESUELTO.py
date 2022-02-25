"""
    Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

"""

inum = input("por favor introduce un numero: ")
num = int(inum)

for i in range(1, num+1, 2) :
    print(i, end=", ")

