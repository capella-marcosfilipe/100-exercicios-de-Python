from time import sleep

valor1 = float(input('Digite o 1º valor: '))
valor2 = float(input('Digite o 2º valor: '))
resp = 0
while resp != 5:
    print('=' * 20)
    resp = int(input('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nEscolha uma opção: '))
    if resp == 1:
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
        sleep(1)
    elif resp == 2:
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
        sleep(1)
    elif resp == 3:
        if valor1 > valor2:
            print(f'{valor1} é MAIOR que {valor2}.')
        else:
            print(f'{valor2} é MAIOR que {valor1}.')
        sleep(1)
    elif resp == 4:
        print('=' * 20)
        valor1 = float(input('Digite o 1º valor: '))
        valor2 = float(input('Digite o 2º valor: '))
    elif resp not in [1, 2, 3, 4, 5]:
        print('INVÁLIDO. Escolha outra opção!')
        sleep(1)
print('PROGRAMA ENCERRADO!')
