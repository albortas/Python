# Ejemplo Valor Dentro de Rango
# Definimos variables
minimo, maximo = 0, 5

numero = int(input('Proporcione un numero: '))

dentro_rango = numero >= minimo and numero <= maximo
print(f'Valor dentro de Rango: {dentro_rango}')

dentro_rango2 = minimo <= numero <= maximo
print(f'Valor dentro de Rango: {dentro_rango2}')