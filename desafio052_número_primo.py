num = int(input('Digite um número: '))
primo = 0
'''for c in range (num, 0, -1):
    if num % c == 0:
        primo += 1
'''
# Solução de Guanabara
for c in range(1, num + 1):
    # Para colorir os números
    if num % c == 0:
        # Se for divisível fica em amarelo
        print('\033[33m', end='')
        primo += 1
    else:
        # Se não for divisível fica em vermelho
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} foi divisível {primo} vezes')
if primo == 2:
    print(f'O número {num} é PRIMO!')
else:
    print(f'O número {num} NÃO É PRIMO!')
