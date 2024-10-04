
def factorial(numero):
    #Caso base, factorial 0! = 1 or 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else:
        factorial_parcial = numero*factorial(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

if __name__ == '__main__':
    numero = 5
    resultado = factorial(numero)
    print(f'El factorial de {numero} es: {resultado}')
        