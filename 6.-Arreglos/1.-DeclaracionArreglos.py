#Arreglos en Python
#Declarar un arreglo (list)
numero_arreglo = [13, 14, 'Hola']
#Modificar los valores del arreglo
print(f'Arreglo[0] = {numero_arreglo[0]}')
print(f'Arreglo[1] = {numero_arreglo[1]}')
print(f'Arreglo[2] = {numero_arreglo[2]}')
numero_arreglo[0] = 15
numero_arreglo[1] = 22
numero_arreglo[2] = 'Adios'
""" numero_arreglo.append(13)
numero_arreglo.append(14)
numero_arreglo.append('Hola') """

# Accedemos a los valores del arreglo (list)
""" print(f'Arreglo[0] = {numero_arreglo[0]}')
print(f'Arreglo[1] = {numero_arreglo[1]}')
print(f'Arreglo[2] = {numero_arreglo[2]}') """

#Iterar arreglos
for i in numero_arreglo:
    print(f'Arreglo {i}')

#Iteramos de otra forma la lista
print(f'\nImprimimos de otra forma la lista')
for indice, elemento in enumerate(numero_arreglo):
    print(f'Arreglo[{indice}] = {elemento}')