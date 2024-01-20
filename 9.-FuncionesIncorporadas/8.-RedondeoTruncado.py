import math
# Redondeo y truncado
numero = float(input('Proporcione un numero flotante: '))
print(f'Valor original: {numero}')

#round() - redondea al entero par mas cercano si termina en .5
redondeo = round(numero)
print(f'Redeondeo: {redondeo}')

#Truncado, elimina decimales
truncado = math.trunc(numero)
print(f'Truncado: {truncado}')

#math.floor() redondea al entero inferior mas cercano
floor = math.floor(numero)
print(f'Floor: {floor}')

#math.ceil() redondea al entero superior mas cercano
ceil = math.ceil(numero)
print(f'Ceil: {ceil}')