"""
    Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


"""

clave = "hola"

user = input("Introduce la contraseña\n")

if user == clave:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")


