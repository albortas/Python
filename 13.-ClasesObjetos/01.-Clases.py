#Definicion de una clase
class Persona:
    
    def inicializar_persona(self, nombre : str, apellido : str):
        #Crear los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        
#Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona() #Creamos un objeto vacio en memoria
    persona1.inicializar_persona('Layla','Acosta')
    persona1.mostrar()
    persona2 = Persona()
    persona2.inicializar_persona('Ian','Sanchez')
    persona2.mostrar()