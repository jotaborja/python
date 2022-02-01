""""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


"""
print("Bienvenido")
balancefinal = input("Cuanto dinero depositaste? ")
balancefinal = float(balancefinal)

first_year = round((balancefinal * 4) / 100, 2)
second_year = round((balancefinal * 8) / 100, 2)
third_year = round((balancefinal * 12) / 100, 2)

print("Tus intereses en el primer año seran: ", first_year)
print("Tus intereses en el segundo año seran: ", second_year)
print("Tus intereses en el tercer año seran: ", third_year)

