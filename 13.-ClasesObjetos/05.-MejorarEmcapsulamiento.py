# Definimos la clase coche
class Coche:
    #Costructor
    def __init__(self, marca: str, modelo: str, color:str = 'Blanco') -> None:
        self._marca = marca
        self._modelo = modelo
        self._color = color
    
        
    #Metodo get/set
    @property # Definir el metodo get de manera mas pythonica
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca: str):
        self._marca = marca
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo:str):
        self._modelo = modelo
        
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color:str):
        self._color = color
        
    #Metodo
    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')
        
        
#Programa principal
if __name__ == '__main__':
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    
    # No deberiamos acceder a los atributos que no sean publicos
    """ coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2' #Esto no es buena practica
    coche1.__color = 'Azul 2' #Ignora la modificacion
    coche1.conducir()
    coche1._Coche__color = 'Azul 3' # Es una mala practica
    coche1.conducir() """
    
    #Para modificar
    coche1.marca = 'Toyota 2'
    coche1.modelo ='Yaris 2'
    coche1.color = 'Azul 2'
    #Interntar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo')
    coche1.atributo2 = 'nuevo atributo 2'
    #Conocer los atributos de mi objeto
    print(f'Atributos del objeto 1: {coche1.__dict__}')
    coche1.conducir()
    print(coche1.nuevo_atributo)