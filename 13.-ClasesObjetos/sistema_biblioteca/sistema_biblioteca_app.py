from biblioteca import Biblioteca
print('Bienvenidos a la Bibliote Nacional')

bibl1 = Biblioteca('Biblioteca Nacional')

bibl1.agregar_libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
bibl1.agregar_libro('El amor en los tiempos del colera', 'Gabriel García Márquez', 'Ficción')
bibl1.agregar_libro('Pedro Páramo', 'Juan Rufalo', 'Ficción')
print()
bibl1.buscar_libros_por_autor('Gabriel García Márque')
print()
bibl1.buscar_libros_por_genero('Ficción')
print()