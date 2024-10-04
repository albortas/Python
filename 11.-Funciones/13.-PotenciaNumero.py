


def potencia(numero,exponente):
    #Caso base a^0 = 1
    if exponente == 0:
        print(f'El {numero} elevado a {exponente} es: 1')
        return 1
    else:
        resul_parcial = numero*potencia(numero,exponente - 1)
        print(f'El {numero} elevado a {exponente} es: {resul_parcial}')
        return resul_parcial
    
numero, exponente = 2,10
resultado = potencia(numero,exponente)
        