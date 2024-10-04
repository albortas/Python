
numero_filas = int(input('Proporciona el numero de filas: '))

for fila in range(numero_filas+1):
    e_blanco = ' '*(numero_filas-fila)
    e_asterisco = '*'*(2*fila-1)
    print(f'{e_blanco}{e_asterisco}')