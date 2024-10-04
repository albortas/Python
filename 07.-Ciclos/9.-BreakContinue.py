print('Break')
for numero in range(1,10+1):
    if numero % 2 == 0:
        print(numero)
        break
    
print('Continue')
for numero in range(1,10+1):
    if numero % 2 == 1:
        continue
    print(numero)