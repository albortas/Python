def imprimir(datos):
    print(f'\tNombre: {datos['nombre']}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}')

def mostra_inventario(productos):
    for llave, valor in productos.items():
        print(f'Producto Id: {llave}')
        imprimir(valor)

def agregar_producto():
    nombre = input('Nombre del Producto: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    productos[len(productos)+1] = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

def busca_id():
    id_buscar = int(input('Proporcione un Id: '))
    for llave,valor in productos.items():
        if llave == id_buscar:
            print(f'Producto Id: {llave}')
            imprimir(valor)
            return
    print(f'Producto con Id: {id_buscar} no encontrado')

menu = '''
---Menu---
    1. Mostrar Inventario
    2. Agregar nuevo producto
    3. Buscar producto por Id
    4. Salir
'''
condicion = False

productos = {
    1 : {
        'nombre': 'Camisa',
        'precio': 25.99,
        'cantidad': 50
    },
    2 : {
        'nombre': 'Pantalones',
        'precio': 39.99,
        'cantidad': 30
    },
    3 : {
        'nombre': 'Zapatos',
        'precio': 49.99,
        'cantidad': 20
    }
}

while not(condicion):
    print(menu)
    op = int(input('Proporcione una opción: '))
    if op == 1:
        print('\n***Inventario del almacen***')
        mostra_inventario(productos)
    elif op == 2:
        print('\n****Agregar nuevo Producto****')
        agregar_producto()
    elif op == 3:
        print('\n***Buscar por id***')
        busca_id()    
    elif op == 4:
        print('\nHasta luego!')
        condicion = True
    else:
        print(f'Opcion proporcionada no valida: {op}')

    