MAXIMO = 5
numero = 1
aux = 0

while numero <= MAXIMO:
    print(f'{aux} + {numero}')
    aux += numero;
    print(aux)
    numero += 1

print(aux)