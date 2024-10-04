monto = float(input('Monto de su compra: '))
miembro = input('Eres mienbro (Si/No): ')
condicion = miembro.lower().strip() == 'si'

descuento = 0.0

if condicion:
    if monto >= 1000:
        descuento = 0.10
    else:
        descuento = 0.05
elif not(condicion):
    if monto >= 1000:
        descuento = 0.03
    else:
        descuento = 0

monto_pagar = monto-monto*descuento
print(f'Descuento: {monto*descuento:.2f}')
print(f'Monto a pagar: {monto_pagar:.2f}')        
