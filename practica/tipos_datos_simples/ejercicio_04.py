"""

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


"""

precio_normal = 3.49
precio_descuento = 3.49 * 60 / 100

pan_ayer = input("Buenos dias, cuantas barras de pan vendiste hoy?")
pan_ayer = float(pan_ayer)

total = precio_descuento * pan_ayer


print("Normalmente el pan cuesta:", precio_normal,"por unidad")
print("Como este pan es de ayer tienes un descuento del 60% entonces el precio del pan por unidad te quedaria en:", precio_descuento)
print("El total es:", total)
