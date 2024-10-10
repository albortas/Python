class Persona:
    # Atributo Clase
    contador_personas = 0
    
    def __init__(self, nombre:str, apellido:str) -> None:
        #Incrementar el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'''Persona: {self.id}
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        
if __name__ == '__main__':
    persona1 = Persona('Gerardo','Perez')
    persona1.mostrar_persona()
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()