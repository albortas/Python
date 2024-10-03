 # Matrices en Python (listas de listas)
 # Declaracion de una matriz
#matriz = [[100, 200, 300],[400, 500, 600]]

#Introducir valores a una matriz
renglones = int(input('Proporciona No. renglones: '))
columnas = int(input('Proporciona No. columnas: '))
#Creamos la matriz
matriz = [0] * renglones
for ren in range(renglones):
    #Por cada renglon, asignamos una lista de m columnas
    matriz[ren] = [0] *columnas

#Solicitar los valores de manera dinamica
for ren in range(renglones):
    for col in range(columnas):
        matriz[ren][col] = int(input(f'Matriz[{ren}][{col}] = '))

# Iterar la matriz
print(f'\nLa matriz es: ')
for i in range(len(matriz)):
    print(f'Renglones {i}')
    for j in range(len(matriz[i])):
        print(f'Matriz[{i}][{j}] = {matriz[i][j]}')
