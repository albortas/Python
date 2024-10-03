# Las cadenas son inmutables

def cambiar_valor(parametro):
    parametro = 'Adios'

argumento = 'Hola'
#argumento[0] = 'A' # Las cadenas son inmutables
print(f'Antes de llamar funcion: {argumento}')
cambiar_valor(argumento)
print(f'Despues de llamar funcion: {argumento}')
