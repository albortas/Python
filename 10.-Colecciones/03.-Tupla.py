# Las tuplas se definen con parentesis()
# La tupla es inmutable
tupla = (1,2,3,4,5)
print(tupla)

for tp in tupla:
    print(tp,end=' ')
print()

#Creacion de un tupla unitaria
tupla_unitaria = 1,
print(f'{tupla_unitaria} de tipo {type(tupla_unitaria)}')

#Tupla anidada
tupla_anidada = (1,2,3,(4,5))
print(tupla_anidada[3])