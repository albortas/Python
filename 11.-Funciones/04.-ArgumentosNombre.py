
def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')


imprimir_persona('Ricardo','Quintana',32)
#Argumentos por nombre
imprimir_persona(nombre='Carlos',apellido='Rojas',edad=43)
#Argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=43,nombre='Pedro',apellido='Ares')
#Argumento con el valor por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos',apellido='Esperancito')