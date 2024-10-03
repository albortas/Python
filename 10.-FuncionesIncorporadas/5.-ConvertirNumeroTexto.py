# Convertir de numero a texto
a, b = 10, 20
# Si son numero se suman
print(a + b)

#Convertir a cadena
#concatenacion = str(a) + str(b)
#concatenacion = a.__str__() + b.__str__()
concatenacion = a.__repr__() + b.__repr__()
print(concatenacion)