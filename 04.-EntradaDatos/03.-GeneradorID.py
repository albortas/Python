from random import randint

nombre = input('Proporcione su nombre: ')
apellido = input('Proporcione su apellido: ')
naciento = input('Año de nacimiento (YYYY): ')
aleatorio = randint(1000,9999)
cadena = nombre[0:2].upper() + apellido[0:2].upper() + naciento[2:5] + str(aleatorio)
print(cadena)