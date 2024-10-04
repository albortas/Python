#Argumentos Variables

#*args recibe una tupla pero debe ser declararse al ultimo
def superheroe(super,nombre,*args):
    print(f'Superheroes: {super} - {nombre} - {args}')

#Llamar la funcion
superheroe('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Telaraña')

#**kwargs - keyword arguments (key, value) como un diccionario
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroes: {nombre} - {args} - Mas Info.: {kwargs}')
    
#Llamar a la funcion
superheroe_superpoderes('Spaiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
    