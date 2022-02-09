"""
    Escribe un programa que repetidamente lea numeros hasta que el usuario introduzca la palabra "done". Cuando "done" es introducido, imprimir el total, count y el promedio de los numeros. Si el usuario introduce cualquier otra cosa en vez de un numero, detecta su error usando try y except y print un mensaje y salta hacia el proximo numero.

"""
num = 0.0
tot = 0.0

while True:
    number = input("Enter a number: ")

    if number == "done" :
        break
    
    try:
        fnumber = float(number)
        num += 1
        tot += fnumber
    except:
        print("invalid input || type done to end program")
        continue
    


print("all done")
print(tot, num, tot/num)
