# Obtener el largo de una cadena
cadena = 'Hola'
print(f'Largo cadena: {len(cadena)}')

print(cadena[0])
cadena = 'Adios'
print(cadena)

# Recorrer los elementos de una cadena
for indice, caracter in enumerate(cadena):
    print(f'{indice} - {cadena[indice]}')
    #print(f'{indice} - {caracter}')

print(enumerate(cadena))