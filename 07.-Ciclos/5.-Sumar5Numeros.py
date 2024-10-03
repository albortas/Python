# Sumar los primeros 5 numeros
#Utilizando el Ciclo For
minimo, maximo, acumulador = 1, 5, 0

print(f'\nUtilizando el Ciclo For')
for numero in range(minimo, maximo +1):
    print(f'{acumulador} + {numero}')
    acumulador += numero
    print(f'Suma parcial: {acumulador}')
print(f'La suma de los primeros {maximo} es: {acumulador}\n')

#Utilizando el Ciclo While
print(f'\nUtilizando el Ciclo While')
acumulador, contador = 0, 1
while contador <= maximo:
    print(f'{acumulador} + {contador}')   
    acumulador += contador
    contador += 1
    print(f'Suma parcial: {acumulador}')
print(f'La suma de los primeros {maximo} es: {acumulador}')