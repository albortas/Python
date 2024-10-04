#Compresion de listas

#una lista de cuadrados
numeros = [1,2,3,4,5,6,7,8]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

pares = [x for x in numeros if x % 2 ==0]
print(pares)

#Lista saludando a cada nombre
nombres = ['Ana', 'Pedro', 'Juan']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)