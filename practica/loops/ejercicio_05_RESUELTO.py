"""

    Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


"""

inum = input("cuanto quieres invertir? ")
iinteres = input("A que porcentaje de interes? ")
itime = input("por cuanto tiempo? ")

num = float(inum)
interes = float(iinteres)
years = int(itime)

for i in range(years):
    num *= 1 + interes / 100
    print("Capital tras " + str(i+1) + " años" + str(round(num,2)))
