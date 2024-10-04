

def sumar(*args):
    total = 0
    for x in args:
        total += x
    return total

resultado = sumar(1,2,3,4,5)
print(resultado)
