#Diccionario
persona = {'nombre': 'Juan', 'edad': 25, 'e_civil': True}
print(persona)

#Aceder  los elmentos del dicionario
print(f'{persona['nombre']}')
print(f'{persona.get('edad')}')
print(f'{persona["e_civil"]}')

#Modificar o Agregar un valor de diccionario
persona['edad'] = 35
print(persona)

persona['profesion'] = 'ingeniero'
print(persona)

#Eliminar un elmento
del persona['e_civil']
print(persona)

persona.pop('profesion')
print(persona)

#Iterar los elmentos
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

#Obtener los valores
for valor in persona.values():
    print(f'-Valor: {valor}')

#Obtener las llaves 
for llave in persona.keys():
    print(f'-Llave: {llave}')