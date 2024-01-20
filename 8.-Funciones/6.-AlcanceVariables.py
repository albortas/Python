#Alcance de variables

variable_global = 5
a = 10
variable_global = 10

#definimos una funcion
def mi_funcion(variable_local):
    print(variable_local)
    variable_local = 20
    print(variable_global)
    #Accedemos a la variable global
    #global a
    a = 30
    print(a)


mi_funcion(variable_global)
print(f'Valiable global: {variable_global}')
print(f'Valiable global a: {a}')