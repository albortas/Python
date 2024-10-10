# Definimos la clase coche
class Coche:
    #Costructor
    def __init__(self, marca: str, modelo: str, color:str = 'Blanco') -> None:
        # atributo con _ esta protegido
        # atributo con __ es privado
        # atributo y sin barra baja es publico
        self._marca = marca 
        self._modelo = modelo
        self._color = color
    
    #Metodo
    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')
        
    #Metodo get/set
    def get_marca(self):
        return self._marca
    def set_marca(self, marca: str):
        self._marca = marca
    def get_modelo(self):
        return self._modelo
    def set_modelo(self, modelo:str):
        self._modelo = modelo
    def get_color(self):
        return self._color
    def set_color(self, color:str):
        self._color = color
        
        
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
    coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()