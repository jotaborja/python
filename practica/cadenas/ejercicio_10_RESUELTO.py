"""

    Ejercicio 10

Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

"""

productos = input("introduce los productos que compraste separados por una ',' : ")
producto = productos.replace(",", "\n")

print(producto)