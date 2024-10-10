#Definicion de una clase
class Persona:
    
    #Constructor
    def __init__(self, nombre:str, apellido:str) -> None:
        #Crear los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Dir. memoria persona1: {id(self)}
        Dir. memoria hex persona1: {hex(id(self))}''')
        
#Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla','Acosta')
    persona1.mostrar()
    print(f'Dir. memoria persona1: {id(persona1)}')
    #convertimos a hexadecimal
    print(f'Dir. memoria hex persona1: {hex(id(persona1))}')
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar()
    print(f'Dir. memoria hex persona2: {hex(id(persona2))}')