def persona_mayuscula(nombre,apellido,edad):
    return nombre.upper(), apellido.upper(), edad

#Programa principal
nombre, apellido, edad = persona_mayuscula('Sandra','Jimenez',42)
print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')