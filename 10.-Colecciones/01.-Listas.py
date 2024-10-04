#Listas
lista = [1,2,3,4,5]
print(lista)

#Largo de la lista
largo = len(lista)
print(largo)

#Acceder a los elementos de la lista por indices
print(f'Acedemos al indice 4: {lista[4]}')
print(f'Acedemos al ultimo indice: {lista[-1]}')

#Modificar los elementos de la lista
lista[1] = 10
print(f'Acedemos al indice 1: {lista[1]}')

#Agregar un nuevo elemento al final de la lista
lista.append(6)
print(lista)

#Añadir un nuevo elemento en un indice
lista.insert(2, 15)
print(lista)

#Eliminar elementos de una lista
lista.remove(5)
print(lista)

#Eliminar por indice
lista.pop(1)
print(lista)

#Eliminar usando la palabra del
del lista[2]
print(lista)

#Obtener una sublista
sublista = lista[0:2]
print(sublista)

#Ordenar una lista asendente
#lista.sort()
#Ordenar de manera desendente
lista.sort(reverse=True)
print(lista)