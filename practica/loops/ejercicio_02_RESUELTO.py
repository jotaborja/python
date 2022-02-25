"""

    Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

"""

iedad = input("Introduce tu edad: ")

edad = int(iedad)

for i in range(edad) : 
    print("Haz cumplido " + str(i+1) + "años")