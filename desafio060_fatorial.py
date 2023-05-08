num = int(input('Fatorial de: '))
resultado = cont = 1
while cont <= num:
    resultado *= cont
    cont += 1
print(f'O fatorial de {num} é {resultado}')
