#Sentencia if-else Python

mi_numero = int(input('Proporcione un numero: '))

# Verificamos si el numero es positivo

if mi_numero > 0:
    print(f'Valor positivo: {mi_numero}')
elif mi_numero < 0:
    print(f'Valor Negativo: {mi_numero}')
else:
    print(f'Valor Cero: {mi_numero}')

#Operador ternario
print(f'Positivo') if mi_numero > 0 else print(f'Cero o Negativo')