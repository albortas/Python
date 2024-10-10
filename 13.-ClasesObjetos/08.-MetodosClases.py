class Persona:
    # Atributo Clase
    # Tambien se le conoce como contexto ESTATICO
    contador_personas = 0
    
    def __init__(self, nombre:str, apellido:str) -> None:
        #Incrementar el valor del atributo de clase
        # CONTEXTO DINAMICO
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
    
    #CONTEXTO DINAMICO
    def mostrar_persona(self):
        print(f'''Persona: {self.id}
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        
    #Metodos de clases
    #CONTEXTO ESTATICO
    @staticmethod
    def get_contador_personas_estaticos():
        print('Metodo estático')
        return Persona.contador_personas
    
    @classmethod #esta es la forma mas recomendada para trabajar con python
    def get_contador_persona_class(cls):
        print('Metodo de clase')
        return cls.contador_personas
        
if __name__ == '__main__':
    persona1 = Persona('Gerardo','Perez')
    persona1.mostrar_persona()
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()
    #Acceder al metodo estatico
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    #Podemos aceder desde un objeto al contexto estatico
    #Pero desde CONTEXTO ESTATICO no se puede acceder al CONTEXTO DINAMICO
    print(f'Contador objetos Persona (objeto): {persona1.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estaticos()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_persona_class()}')