
#Multiplicar


# Solicitamos el tamaño del arreglo
no_elementos = int(input('No. Elementos del Arreglo: '))
#creacion del arreglo
arreglo = [0]*no_elementos

#Iteramos para solicitar los valores del arreglo
for indice in range(no_elementos):
    valor = int(input(f'Arreglo[{indice}] = '))
    arreglo[indice] = valor

print(f'\nImprimimos de otra forma la lista')
for indice in range(len(arreglo)):
    print(f'Arreglo[{indice}] = {arreglo[indice]}')