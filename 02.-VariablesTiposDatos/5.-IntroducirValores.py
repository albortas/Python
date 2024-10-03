# Introducir Valores en python
#nombre = input('Proporciona tu nombre: ')
#print(f'Hola {nombre}')

numero_str = input('Proporciona un numero entero: ')
print(f'El numero {numero_str} es de tipo: {type(numero_str)}')

#Lo convertimos a entero
numero = int(numero_str)
print(f'El numero {numero} es de tipo: {type(numero)}')


# Obtenemos directamente en valor entero
entero = int(input('Proporciona un entero: '))
print(f'El numero {entero} es de tipo: {type(entero)}')
