condicion = True

while condicion:
    menu = '''Menu:
    1. Crear cuenta.
    2. Eliminar
    3. Salir'''
    print(menu)
    op = int(input('Escoje un opcion: '))
    if op == 1:
        print('Creando cuenta...')
    elif op == 2:
        print('Eliminado cuenta...')
    elif op == 3:
        print('Saliendo del menu...')
        condicion = False
    else:
        print(f'Opcion erronea: {op}')    