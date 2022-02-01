# escribe un programa que le pregunte al usuario cual es su nombre y lo salude.
def preguntacion(pregunta) :
    pregunta = input("quien eres? ")
    return pregunta

x = preguntacion("pregunta")
print("bienvenido", x)
