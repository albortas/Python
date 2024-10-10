class Aritmetica:
    #Constructor
    def __init__(self,operando1:float ,operando2:float = None) -> None:
        #Atributos
        self.__operando1 = operando1
        self.__operando2 = operando2
        
    #Metodos get/set
    @property
    def operando1(self):
        return self.__operando1
    @operando1.setter
    def operando1(self,operando1: float):
        self.__operando1 = operando1
    @property
    def operando2(self):
        return self.__operando2
    @operando2.setter
    def operando2(self,operando2: float):
        self.__operando2 = operando2
        
    #Metodos
    def sumar(self) -> float:
        return self.__operando1 + self.__operando2
    
    def restar(self) -> float:
        return self.__operando1 - self.__operando2
    
    def multiplicacion(self) -> float:
        return self.operando1 * self.operando2
    
    def division(self) -> float:
        if self.operando2 == 0:
            print('La operacion entre cero no es permitida')
            return
        else:
            return self.operando1 / self.operando2
    
        
if __name__ == '__main__':
    aritmetica1 = Aritmetica(5,7)
    resul = aritmetica1.multiplicacion()
    print(resul)
    aritmetica2 = Aritmetica(8)
    aritmetica2.operando2 = 3
    resul = aritmetica2.multiplicacion()
    print(resul)