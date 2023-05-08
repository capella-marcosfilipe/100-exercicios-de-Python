from random import randint
print('=-' * 15)
print('VAMOS JOGAR IMPAR OU PAR')
print('=-' * 15)
tot = 0
while True:
    valor_player = int(input('Digite um valor: '))
    valor_pc = randint(1, 10)
    soma = valor_player + valor_pc
    player = ' '
    while player not in 'pi':
        player = str(input('Ímpar ou Par? [I/P] ')).strip().lower()[0]
    print(f'Você jogou {valor_player} e o PC {valor_pc}. Total de {soma}.')
    if player == 'p':
        if soma % 2 == 0:
            print('Você VENCEU!')
            tot +=1
        else:
            print('Você PERDEU!')
            break
    elif player == 'i':
        if soma % 2 == 1:
            print('Você VENCEU!')
            tot += 1
        else:
            print('Você PERDEU!')
    print('Vamo jogar novamente...')
    print('=-' * 15)
print(f'GAME OVER! Você venceu {tot} vezes.' if tot != 1 else f'GAME OVER! Você venceu {tot} vez.')
