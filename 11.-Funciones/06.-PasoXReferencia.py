#En Python los objetos se pasan por referencia

def cambiar_valor(parametro):
    parametro[0] = 20

argumento = [10]
print(f'Antes de llamar funcion: {argumento}')
cambiar_valor(argumento)
print(f'Despues de llamar funcion: {argumento}')
