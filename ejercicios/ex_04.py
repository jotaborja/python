"""
    Agarra el siguiente codigo que almacena una string

    str = 'XSPAM-Confidence: 0.8475 '

    Usa find y string slicing para extraer la porcion de la string despues del colon character y despues una la funcion float para convertir la cadena extraida en una numero punto flotante
"""

str = 'X-DSPAM-Confidence: 0.8475'

encuentra = str.find(":")
print(encuentra)

num = str[encuentra+2:]
print(num)

numfloat = float(num)
print(type(numfloat))