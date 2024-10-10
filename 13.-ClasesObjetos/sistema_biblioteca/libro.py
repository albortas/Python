class Libro:
    #constructor
    def __init__(self, titulo: str, autor:str, genero:str) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
    
    # Metodos get/set
    @property
    def titulo(self) -> str:
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo:str) -> None:
        self.__titulo = titulo
    @property
    def autor(self) -> str:
        return self.__autor
    @autor.setter
    def autor(self,autor) -> None:
        self.__autor = autor
    @property
    def genero(self) -> str:
        return self.__genero
    @genero.setter
    def genero(self, genero) -> None:
        self.__genero = genero