def formato_snack(snack):
    cadena = (f'{snack['nombre']} - ${snack['precio']}')
    return cadena

def mostrar():
    for llave, valor in snacks.items():
        print(f'\t- Id: {llave} ->', end=' ')
        print(formato_snack(valor))

def comprar_snack():
    id_comprar = int(input('Que snack quieres comprar (id): '))
    for llave,valor in snacks.items():
        if llave == id_comprar:
            orden.append(valor)
            print('Snack agregado: {Id: ' + str(llave) + ' -> ' + formato_snack(valor) + '}')
            return
    print(f'Snack No encontrado con id: {id_comprar}')
    
def ticket():
    total = 0
    print('\t*** Ticket ***')
    for datos in orden:
        print(f'\t-{formato_snack(datos)}')
        total += datos['precio']
    print(f'\tTOTAL -> ${total}')
            

menu = '''
*** Maquina de Snacks ***
Menú:
    1. Mostrar Snacks
    2. Comprar Snack
    3. Mostrar ticket
    4. Salir'''

snacks = {
    1 : {
        'nombre': 'Papas',
        'precio': 30
    },
    2 : {
        'nombre': 'Refresco',
        'precio': 50
    },
    3 : {
        'nombre': 'Sandwich',
        'precio': 120
    }
}

orden = []

while True:
    print(menu)
    op = int(input('Escoge un opción: '))
    print()
    if op == 1:
        print(f'\t--- Snacks Disponibles ---')
        mostrar()
    elif op == 2:
        comprar_snack()
    elif op == 3:
        ticket()
    elif op == 4:
        print('Hasta Pronto!')
        break
    else:
        print(f'Opción Inválida: {op}')