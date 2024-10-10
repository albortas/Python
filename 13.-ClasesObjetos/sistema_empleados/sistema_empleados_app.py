from empleado import Empleado
from empresa import Empresa
print('*** Sistema de Empleados ***')

# Crear un instancia de una empresa
empresa1 = Empresa('Globlal Mentoring')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('María', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')
# Obtener el total de objetos de tipo empleado
print(f'Total de empledos: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento de ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')

#Eliminar empleado
empresa1.eliminar_empleado(3)
empresa1.contratar_empleado('Juana', 'Ingenieria Electronica')

#Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()