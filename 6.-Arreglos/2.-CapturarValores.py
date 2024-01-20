
arreglo = []

# Solicitamos el tamaño del arreglo
no_elementos = int(input('No. Elementos del Arreglo: '))

#Iteramos para solicitar los valores del arreglo
for indice in range(no_elementos):
    valor = int(input(f'Arreglo[{indice}] = '))
    arreglo.append(valor)

print(f'\nImprimimos de otra forma la lista')
for indice in range(len(arreglo)):
    print(f'Arreglo[{indice}] = {arreglo[indice]}')