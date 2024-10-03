#Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(numero_cadena)
print(numero_entero)

#Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)

#Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Entero {numero_entero} es de tipo {type(numero_entero)}')
print(f'Cadena {numero_cadena} es de tipo {type(numero_cadena)}')

# Convertir a booleano
# Tipo es False en los siguientes casos:
# - Si el valor es 0, cadena vacia, o None.
# Tipo es True en los siguientes casos:
# - Si el valor es distinto de ( 0, cadena vacia, None)

numero_entero = 0
booleano = bool(numero_entero)
print(booleano)
numero_entero = 5
booleano = bool(numero_entero)
print(booleano)
cadena = ''
booleano = bool(cadena)
print(booleano)
cadena = 'Hola'
booleano = bool(cadena)
print(booleano)
a = None
booleano = bool(a)
print(booleano)
