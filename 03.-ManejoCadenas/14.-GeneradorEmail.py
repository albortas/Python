nombre = 'Daniel Alejandro Alborta Garcia'
empresa = 'UMSA'
dominio = 'com.bo'
lista_nombre = nombre.split()
cadena = ''
i = 0
largo = len(lista_nombre)

for lista in lista_nombre:
    if i < largo-1:
        cadena += ''.join(lista.lower()) + '.'
    elif i == largo-1:
        cadena += ''.join(lista.lower())
    i += 1
email = cadena + '@' + empresa.lower() + '.' + dominio
print(email)