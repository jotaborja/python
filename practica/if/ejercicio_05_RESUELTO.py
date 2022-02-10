"""
    Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

"""

iedad = input("Introduce tu edad\n")
isueldo = input("Introduce tu sueldo \n")

edad = float(iedad)
sueldo = float(isueldo)

min_edad = 16
min_sueldo = 1000

if edad > min_edad and sueldo >= min_sueldo : 
    print("Tienes que pagar impuestos")

else: 
    print("Te salvaste  ")

