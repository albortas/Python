
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero)
    else:
        #Caso Recusiva
        print(numero)
        funcion_recursiva(numero - 1)
#Llamamos a la funcion recusiva
funcion_recursiva(5)