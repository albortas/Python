from libro import Libro

class Biblioteca:
    #Constructor
    def __init__(self,nombre:str) -> None:
        self.__nombre = nombre
        self.__libros = []
        
    #Metodos get/set
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre) -> None:
        self.__nombre = nombre
    
    #Metodos
    def agregar_libro(self,titulo:str,autor:str,genero:str) -> None:
        libro = Libro(titulo,autor,genero)
        self.__libros.append(libro)
        
    def mostrar_libro(self,libro:Libro):
        print(f'Libro: Titulo: {libro.titulo}, Autor: {libro.autor}, Genero: {libro.genero}')
        
    def buscar_libros_por_autor(self, autor: str) -> None:
        print(f'Libros de {autor}')
        for libro in self.__libros:
            if libro.autor == autor:
                self.mostrar_libro(libro)

                
    def buscar_libros_por_genero(self, genero: str) -> None:
        print(f'Libros de {genero}')
        for libro in self.__libros:
            if libro.genero == genero:
                self.mostrar_libro(libro)
                
                        
    def mostrar_libros(self) -> None:
        for libro in self.__libros:
            self.mostrar_libro(libro)