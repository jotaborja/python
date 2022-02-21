"""
        Escribe un programa que abra un archivo y extraiga todos los correos que consiga en ese archivo

"""


fhand = open("hola.txt")

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From") :
        continue
    sline = line.split()
    email = sline[1]
    pieces = email.split("@")
    print(pieces)