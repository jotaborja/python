""""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

La formula para el IMC es el peso en kg dividido por la estatura en metros cuadrados.

"""

kg = input("Introduce tu peso en Kg ")
estatura = input("Introduce tu estatura en metros ")

try:
    kg = float(kg)
    estatura = float(estatura)
except:
    print("Introduce tu peso en Kilogramos y tu estatura en Metros ")
    quit()
imc = kg / estatura**2

print("tu indice de masa corporal es ",imc)


