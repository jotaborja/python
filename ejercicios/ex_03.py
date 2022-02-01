"""
    Escribe un programa que repetidamente lea numeros hasta que el usuario introduzca la palabra "done". Cuando "done" es introducido, imprimir el total, count y el promedio de los numeros. Si el usuario introduce cualquier otra cosa en vez de un numero, detecta su error usando try y except y print un mensaje y salta hacia el proximo numero.

"""
num = 0
tot = 0.0

while True:
    number = input("Enter a number: ")
    if number == "done" :
        break
    try:
        number = float(number)
    except:
        print("invalid input")
        continue

print("all done")
print("tot, num, tot/num")
