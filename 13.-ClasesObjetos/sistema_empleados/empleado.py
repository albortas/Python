class Empleado:
    # Atributo de clase
    contador_empleados:int = 0
    # Constructor
    def __init__(self, nombre: str, departamento: str) -> None:
        Empleado.contador_empleados += 1
        self.id_empleado = Empleado.contador_empleados
        self.nombre = nombre
        self.departamento = departamento
        
    
    
    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados