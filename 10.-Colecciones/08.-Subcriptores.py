#Lista de subcriptores
#Para definir un set vacio
#suscriptores = set()
suscriptores = {'luisa@email.com','marcos@email.com','elena@email.com'}
print(suscriptores)

#Verificar si un nuevo subcriptor ya esta en lista
nuevo_suscriptor = 'karla@email.com'
if nuevo_suscriptor in suscriptores:
    print(f'El suscriptos ya se encuentra')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'Se agrego el nuevo suscriptor')
print(suscriptores)

