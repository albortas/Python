
class Persona:
    #atributo de clase se asocia con la clase en si misma y no con los objetos
    atributo_clase:int = 0
    def __init__(self,atributo_instancia:int) -> None:
        self.atributo_instancia = atributo_instancia

#Programa Principal
if __name__ == '__main__':
    print(f'*** Atributos de Clase ***')
    print(f'Atributos de clase: {Persona.atributo_clase}') #Forma correcta de acceder al atributo de clase
    
    #Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributos de clase: {Persona.atributo_clase}')
    
    # Creamos un objeto persona1
    persona1 = Persona(15)
    print(f'Atributos de clase: {persona1.atributo_clase}') # Podemos acceder desde un objeto pero no es bien hacerlo
    print(f'Atributos de instancia: {persona1.atributo_instancia}')
    
    #Creamos un objeto persona2
    persona2 = Persona(30)
    print(f'Atributos de clase: {persona2.atributo_clase}') # Podemos acceder desde un objeto pero no es bien hacerlo
    print(f'Atributos de instancia: {persona2.atributo_instancia}')