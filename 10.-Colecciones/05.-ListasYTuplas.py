
#Combinacion de Listas y Tuplas

productos = [
    ('P001','Camisa', 20.00),
    ('P002','Jeans',30.00),
    ('P003','Sudadera',40.00)
]

precio_total = 0

for producto in productos:
    id,descipcion,precio = producto
    print(f'id: {id}, descripcion: {descipcion}, precio: {precio}')
    precio_total += precio
print(f'Precio Total: {precio_total}')