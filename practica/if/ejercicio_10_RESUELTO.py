"""

    Ejercicio 10

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

"""

veg = "Pimenton y Tofu "
noveg = "Pepperoni, jamon y salmon "
pizzabase = "Pizza con queso mozarella, tomate y "

preg = input("Quieres una pizza vegetariana? Y / N\n")

if preg.lower() == "y" :
    print("Estos son los ingredientes de los que disponemos, puedes escoger uno para añadirlo a la pizza:", veg)
    vegg = input("Escoje un ingrediente: \n")
    if vegg.lower() == "pimenton":
        print("Tu pizza es vegetariana y tendra:", pizzabase + vegg)
    elif vegg.lower() == "tofu":
        print("Tu pizza es vegetariana y tendra:", pizzabase + vegg)
    else: 
        print("Escribe un ingrediente valido!")
        quit()
else :
    print("Estos son los ingredientes de los que disponemos, puedes escoger uno para añadirlo a la pizza:", noveg)
    novegg = input("Escoje un ingrediente: \n")
    if novegg.lower() == "pepperoni":
        print("Tu pizza no es vegetariana y trae:", pizzabase + novegg)
    elif novegg.lower() == "jamon" :   
        print("Tu pizza no es vegetariana y trae:", pizzabase + novegg)
    elif novegg.lower() == "salmon":
        print("Tu pizza no es vegetariana y trae:", pizzabase + novegg)





