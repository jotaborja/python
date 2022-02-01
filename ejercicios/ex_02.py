""" escribe un programa que le pregunte al usuario cuantas horas trabajo y cuanto le pagan cada hora y que devuelva 
la cantidad que le deben pagar """

""" **** ACTUALIZACION EJERCICIO 3 *****

    Re escribe tu programa para darle a los empleados si tienen mas de 40 horas de trabajo un bono de 1.5 cada hora.
"""

""""
    *** ACTUALIZACION EJERCICIO 4 ***
    
    Re escribe tu programa usando un try y un except para que tu progama maneje los inputs no numericos de manera correcta, print un mensaje y cierre el programa.

    *** ACTUALIZACION EJERCICIO 5 ***

    Re escribe el programa con el bono de sobretiempo y crea una funcion llamada computepay que tomara dos parametros (hours y rate)
"""


def computepay(hours, rate):


    # print(horas_trabajo, valor_hora)

    if hours > 40 :
        print("Overtime")
        pago_normal = hours * rate
        pago_overtime = (hours - 40.0) * (rate * 0.5)
        print(pago_normal, pago_overtime)
        total = pago_normal + pago_overtime
        return total
    else :
        print("Regular")
        total = hours * rate
        return total

hours = input("Cuantas horas trabajaste? ")
rate = input("A cuanto te pagan la hora? ")
try : 
    hours = float(hours)
    rate = float(rate)
except:
    print("Por favor introduzca un numero")
    quit() # importante para que el programa deje de funcionar


x = computepay(hours, rate)
print("Pay:",x)

