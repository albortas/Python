# Ciclo While

contador, repeticiones = 0, 5

while contador < repeticiones:
    print(f'Buenos dias... {contador}')
    contador += 1
    condicion = contador < repeticiones
    print(f'{contador} < {repeticiones} -> {condicion}')
else:
    print('Fuera del ciclo while')