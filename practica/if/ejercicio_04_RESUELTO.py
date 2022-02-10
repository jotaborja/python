"""
    Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


"""

inumero = input("Introduce un numero y te digo si es par o impar\n")

num = float(inumero)

if num % 2 == 0:
    print(num)
    print("Es par!")
    
else: 
    print(num)
    print("Es impar :(")