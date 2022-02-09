"""
    Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

"""
n_letras = 0
nombre = input("Introduce tu nombre: ")
# print("Bienvenido", nombre)

# for letter in nombre:
#     n_letras = n_letras + 1

# print(nombre.upper(), "tiene: ", n_letras, "letras en el")

print(nombre.upper(), "tiene: ", len(nombre), "letras en el")