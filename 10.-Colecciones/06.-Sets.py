#Set elementos unicos, no tiene elmentos duplicados
mi_set = {1,2,3,4,5,4}
print(mi_set)

#Agregar elementos al set
mi_set.add(6)
print(mi_set)

#Eliminar elementos
mi_set.remove(3)
print(mi_set)

#Iterar
for elemeto in mi_set:
    print(elemeto, end=' ')
print()

#Comprobar si existe un elemento en el set
print(f'{1 in mi_set}')

#Obtener la logitud del set
print(len(mi_set))