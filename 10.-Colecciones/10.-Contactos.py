# Agenda Contactos
agendas = {
    'Carlos': {
        'telefono': 78913462,
        'email': 'carlos@email.com',
        'pais': 'Chile'
    },
    'Maria': {
        'telefono': 78943462,
        'email': 'maria@email.com',
        'pais': 'Peru'        
    }
}

print(agendas)

#Aceder a la informacion
print(agendas['Maria']['telefono'])
print(agendas['Maria']['email'])
print(agendas['Carlos']['email'])

#Agregar un nuevo contacto
agendas['Ana'] = {
    'telefono': 79943462,
    'email': 'ana@email.com',
    'pais': 'Bolivia'  
}

print(agendas)

#eliminar
agendas.pop('Carlos')
print(agendas)

#Mostramos los contactos
for nombre, detalles in agendas.items():
    print(nombre)
    print(detalles['telefono'])