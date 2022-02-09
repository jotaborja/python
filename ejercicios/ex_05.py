"""

escribe un programa que lea a traves de un file e imprima el contenido del file linea por linea todas en mayusculas.

"""


fname = input("Enter a file name: ")

try : 
    fhandle = open(fname)

except :
    print("Introduzca un nombre de archivo valido")
    quit()

for line in fhandle :

    line = line.rstrip()
    print(line.upper())