# Imprimir los primeros 10 numeros de 3 en 3

maximo, minimo = 10, -10
print('Incrementos de 3 en 3')
numeros_asc = range(1, maximo + 1, 3)
for numero in numeros_asc:
    print(numero, end=' ')

print(f'\nDecremento de 3 en 3')
numeros_des = range(1, minimo -1, -3)
for numero in numeros_des:
    print(numero, end=' ')
print()