"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


"""


clown = 112
doll = 75

print("Bienvenido")

numbers_of_clowns = input("Cuantos payasos vendiste? ")
numbers_of_dolls = input("Cuantas muñecas vendiste? ")

try: 
    numbers_of_clowns = float(numbers_of_clowns)
    numbers_of_dolls = float(numbers_of_dolls)
except:
    print("Por favor introduce un numero")
    quit()

weight_clown = clown * numbers_of_clowns
weight_doll = doll * numbers_of_dolls
total_weight = weight_doll + weight_clown


print("El peso total de los payasos es: ", weight_clown)
print("El peso total de las muñecas es: ", weight_doll)
print("El peso total del paquete es: ", total_weight,"gramos")
