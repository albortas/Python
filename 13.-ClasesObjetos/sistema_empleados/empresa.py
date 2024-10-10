from empleado import Empleado

class Empresa:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.empleados = []
        
    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)
        
    def eliminar_empleado(self, id):
        self.empleados.pop(id-1)
    
    def obtener_numero_empleados_departamento(self, departamento:str):
        contador_empleados_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_departamento += 1
        return contador_empleados_departamento
    
    def obtener_total_empleados(self):
        print(f'\nTotal de Empleados para la empresa: {self.nombre}')
        for empleado in self.empleados:
            print(f'''Empleado {empleado.id_empleado}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}''')