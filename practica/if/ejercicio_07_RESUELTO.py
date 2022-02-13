"""

    Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

"""

renta = input("Cuanto haces al año? ")

frenta = float(renta)

if frenta < 10000 :
    porcentaje = "5%"
elif frenta < 20000 : 
    porcentaje ="15%"
elif frenta < 35000 : 
    porcentaje = "20%"
elif frenta < 60000 : 
    porcentaje = "30%"
else :
    porcentaje = "45%"

print("Debes pagar una comision del: " + porcentaje)